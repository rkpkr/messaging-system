import os
from twilio.rest import Client

account_sid = os.environ.get['TWILIO_ACCOUNT_SID']
auth_token = os.environ.get['TWILIO_AUTH_TOKEN']

client = Client(account_sid, auth_token)

def send_messages(my_number, to_numbers, message):
	for n in to_numbers:
		client.messages.create(
			to=n,
			from_=my_number,
			body=message)

def parse_numbers(in_file):
	if in_file.lower().endswith('.txt'):
		pass
	elif in_file.lower().endswith('.csv'):
		pass
	elif in_file.lower().endswith('.xls'):
		pass