import os
from . import db
from .models import Contact
from twilio.rest import Client

account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
my_number = os.environ.get('TWILIO_PHONE')

client = Client(account_sid, auth_token)

def get_contacts():
	contact_list = []
	for row in db.session.query(Contact.phnumber).all():
		contact_list.append(row.phnumber)
	return contact_list

def format_contacts(numbers):
	formatted_numbers = []
	for n in numbers:
		# the + symbol is necessary for Twilio, and the 1 is the international
		# code for U.S. phone numbers
		# change it depending on the country of the phone numbers
		formatted_numbers.append("+1" + n)
	return formatted_numbers

def send_messages(from_number, to_numbers, message):
	for n in to_numbers:
		client.messages.create(
			to=n,
			from_=from_number,
			body=message)


if __name__ == "__main__":
	pass