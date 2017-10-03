from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class Login(FlaskForm):
	user = StringField('username', validators=[DataRequired()])
	password = StringField('password', validators=[DataRequired()])