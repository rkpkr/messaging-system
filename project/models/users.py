from flask_login import UserMixin

class User(UserMixin):

	def __init__(self, name, password):
		self.name = name
		self.password = password