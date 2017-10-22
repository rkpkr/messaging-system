import os
import re
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
		is_formatted = re.search(r'\+\d{11}', n)
		is_valid = re.search(r'(\(?\d{3}\D{0,3}\d{3}\D{0,3}\d{4}).*?', n)
		if is_formatted:
			formatted_numbers.append(n)
		elif is_valid:
			# add + symbol and international code to phone number for Twilio
			f_number = "+1"
			for c in n:
				if c.isdigit():
					f_number = f_number + c
			formatted_numbers.append(f_number)
	return formatted_numbers

def send_messages(from_number, to_numbers, message):
	for n in to_numbers:
		client.messages.create(
			to=n,
			from_=from_number,
			body=message)

def format_number(phonenumber):
	clean_number = ''
	for c in phonenumber:
		if c.isdigit():
			clean_number = clean_number + c
	return clean_number


if __name__ == "__main__":
	pass