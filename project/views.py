from . import app, db, login_manager
from flask import render_template, request, flash, redirect, url_for
from flask_login import login_user, logout_user, current_user, login_required
from .models import User, Contact
from .forms import Register, Login, SendMessages, AddContact, RemoveContact
from bcrypt import hashpw, gensalt
from .controls import get_contacts, format_contacts, my_number, send_messages, format_number


@app.route('/test')
def test():
	return render_template('test.html', title='Test Page')

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
	return render_template('registration.html', title='Registration', form=register_form)

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
			return redirect('/send')
	return render_template('login.html', title='Login', form=form)

@app.route('/logout')
@login_required
def logout():
	user = current_user
	user.authenticated = False
	db.session.add(user)
	db.session.commit()
	logout_user()
	return redirect('/')

@app.route('/send', methods=['GET', 'POST'])
@login_required
def send():
	form = SendMessages()
	if form.validate_on_submit():
		msg = form.message.data
		contacts = get_contacts()
		f_contacts = format_contacts(contacts)
		print(f_contacts)
		#send_messages(my_number, f_contacts, msg)
	return render_template('send.html', title='Send Message', form=form)

@app.route('/manage', methods=['GET', 'POST'])
@login_required
def manage():
	addForm = AddContact()
	remForm = RemoveContact()
	if addForm.validate_on_submit() and addForm.addSubmit.data:
		try:
			dupe_check = Contact.query.filter_by(phnumber=addForm.phnumber.data).first()
			if dupe_check is not None:
				flash('Phone number already exists.')
			else:
				new_number = format_number(addForm.phnumber.data)
				new_contact = Contact(addForm.fname.data, addForm.lname.data, new_number)
				db.session.add(new_contact)
				db.session.commit()
				return redirect('/manage')
		except IntegrityError:
			db.session.rollback()
			flash('ERROR! Phone number already exists.')
	elif remForm.validate_on_submit() and remForm.remSubmit.data:
		try:
			contact = Contact.query.filter_by(phnumber=format_number(remForm.pnumber.data)).first()
			db.session.delete(contact)
			db.session.commit()
			return redirect('/manage')
		except IntegrityError:
			db.session.rollback()
			flash('ERROR! Phone number not found.')
	return render_template('manage.html', title='Contact Management', addForm=addForm, remForm=remForm)