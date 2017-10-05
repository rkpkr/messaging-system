from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired

class Login(FlaskForm):
	user = StringField('username', validators=[DataRequired()])
	password = PasswordField('password', validators=[DataRequired()])