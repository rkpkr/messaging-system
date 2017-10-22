from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, DataRequired, EqualTo

class Register(FlaskForm):
	username = StringField('Username', validators=[DataRequired(),
		Length(min=4, max=15)])
	passwd = PasswordField('Password', validators=[DataRequired(),
		Length(min=6, max=30)])
	confirm = PasswordField('Repeat Password', validators=[DataRequired(),
		EqualTo('passwd')])

class Login(FlaskForm):
	user = StringField('Username', validators=[DataRequired(),
		Length(min=4, max=15)])
	password = PasswordField('Password', validators=[DataRequired(),
		Length(min=6, max=30)])

class SendMessages(FlaskForm):
	message = StringField('Message:', validators=[DataRequired()])
	submit = SubmitField(' ')

class AddContact(FlaskForm):
	fname = StringField('First Name', validators=[DataRequired()])
	lname = StringField('Last Name', validators=[DataRequired()])
	phnumber = StringField('Phone Number', validators=[DataRequired()])
	addSubmit = SubmitField('Add')

class RemoveContact(FlaskForm):
	pnumber = StringField('Phone Number', validators=[DataRequired()])
	remSubmit = SubmitField('Remove')