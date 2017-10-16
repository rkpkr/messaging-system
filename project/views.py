from . import app, db, login_manager
from flask import render_template, request, flash, redirect, url_for
from flask_login import login_user, logout_user, current_user, login_required
from .models import User
from .forms import Register, Login, SendMessages
from bcrypt import hashpw, gensalt
from .controls import get_contacts, format_contacts, my_number, send_messages


@app.route('/test')
def test():
	return render_template('test.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
	register_form = Register()
	if request.method == 'POST':
		if register_form.validate_on_submit():
			try:
				new_user = User(register_form.username.data,
					hashpw((register_form.passwd.data).encode(), gensalt()))
				new_user.authenticated = True
				db.session.add(new_user)
				db.session.commit()
				flash('Registration Successful!')
				return redirect('/login')
			except IntegrityError:
				db.session.rollback()
				flash('ERROR! User already exists.')
	return render_template('registration.html', form=register_form)

@app.route('/login', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def login():
	form = Login()
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.user.data).first()
		if user is not None and user.password_check(form.password.data):
			user.authenticated = True
			db.session.add(user)
			db.session.commit()
			login_user(user)
			flash('Logged in successfully')
			return redirect('/main')
	return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
	user = current_user
	user.authenticated = False
	db.session.add(user)
	db.session.commit()
	logout_user()
	return redirect('/')

@app.route('/main', methods=['GET', 'POST'])
@login_required
def main():
	form = SendMessages()
	if form.validate_on_submit():
		msg = form.message.data
		contacts = get_contacts()
		f_contacts = format_contacts(contacts)
		#send_messages(my_number, f_contacts, msg)
	return render_template('main.html', form=form)