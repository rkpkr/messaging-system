from . import db

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
    password_plaintext = db.Column(db.String, nullable=False)  # TEMPORARY

    def __init__(self, username, password_plaintext):
        self.username = username
        self.password_plaintext = password_plaintext
