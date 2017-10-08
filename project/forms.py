from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import Length, DataRequired, EqualTo

class Register(FlaskForm):
	username = StringField('username', validators=[DataRequired(),
		Length(min=6, max=15)])
	passwd = PasswordField('password', validators=[DataRequired(),
		Length(min=6, max=30)])
	confirm = PasswordField('Repeat Password', validators=[DataRequired(),
		EqualTo('password')])

class Login(FlaskForm):
	user = StringField('username', validators=[DataRequired(),
		Length(min=6, max=15)])
	password = PasswordField('password', validators=[DataRequired(),
		Length(min=6, max=30)])