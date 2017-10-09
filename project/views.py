from . import app, db
from flask import render_template, request, flash, redirect, url_for
from .models import User
from .forms import Register, Login

@app.route('/test')
def test():
	test_user = User('aaa','bbb')
	db.session.add(test_user)
	db.session.commit()
	return render_template('test.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
	register_form = Register()
	if request.method == 'POST':
		if register_form.validate_on_submit():
			try:
				new_user = User(register_form.username.data, register_form.passwd.data)
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
		flash('Login requested for {0}'.format(form.user.data))
		return redirect('/main')
	return render_template('login.html', form=form)

@app.route('/main', methods=['GET', 'POST'])
def main():
	return render_template('main.html')