from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, DataRequired, EqualTo

class Register(FlaskForm):
	username = StringField('username', validators=[DataRequired(),
		Length(min=4, max=15)])
	passwd = PasswordField('passwd', validators=[DataRequired(),
		Length(min=6, max=30)])
	confirm = PasswordField('Repeat Password', validators=[DataRequired(),
		EqualTo('passwd')])

class Login(FlaskForm):
	user = StringField('username', validators=[DataRequired(),
		Length(min=4, max=15)])
	password = PasswordField('password', validators=[DataRequired(),
		Length(min=6, max=30)])

class SendMessages(FlaskForm):
	message = StringField('message', validators=[DataRequired()], default=\
		'Enter message to send')
	submit = SubmitField()