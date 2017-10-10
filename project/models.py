from . import db
from sqlalchemy.ext.hybrid import hybrid_method
from bcrypt import checkpw

class Contact(db.Model):

	__tablename__ = "contacts"

	id = db.Column(db.Integer, primary_key=True)
	fname = db.Column(db.String, nullable=False)
	lname = db.Column(db.String, nullable=False)
	phnumber = db.Column(db.String, nullable=False)

	def __init__(self, fname, lname, phnumber):
		self.fname = fname
		self.lname = lname
		self.phnumber = phnumber


class User(db.Model):

	__tablename__ = 'users'

	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	username = db.Column(db.String, unique=True, nullable=False)
	password = db.Column(db.Binary(60), nullable=False)  
	authenticated = db.Column(db.Boolean, default=False)

	@hybrid_method
	def password_check(self, password):
		return checkpw(password.encode(), self.password)

	@property
	def is_authenticated(self):
		return self.authenticated

	@property
	def is_active(self):
		return True

	@property
	def is_anonymous(self):
		return False

	def get_id(self):
		return str(self.id)

	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.authenticated = False
