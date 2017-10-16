from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Initialize and load config
app = Flask(__name__)
app.config.from_object('config')

# Initialize the database ORM with SQLAlchemy
db = SQLAlchemy(app)

#Initialize flask-login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

from .models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.filter(User.id == int(user_id)).first()

from . import views, controls