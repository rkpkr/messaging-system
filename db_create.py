from project import db
from project.models import Contact, User
from bcrypt import hashpw, gensalt

# drop existing database tables - temporary workaround
# remove if you value your db data
# integrate a migration tool if you want to keep your data...
# ...when you change the data models for your database
db.drop_all()

# create database and database table
db.create_all()

# populate database with initial entries in both tables
# creates an admin account with account name 'admin',
# and password 'password'
person1 = Contact('Jenny',' ','867-5309')
user1 = User('admin', hashpw(b'password', gensalt()))

db.session.add(person1)
db.session.add(user1)

db.session.commit()