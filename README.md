# messaging-system
Combines Flask and Twilio to create a messaging service that will send out text messages to a list of contacts.

##Installation and Setup
-----------
This was written in Python 3. Check the requirements.txt for dependencies used. 

I used a postgres database while working on this, but I don't think it would be that difficult to tweak
it to use a different database. At any rate, you'll need to create a config.py file in the top directory
(where run.py is) with the following values:

* WTF_CSRF_ENABLED = True
* SECRET_KEY = 'your secret key goes here'
* SQLALCHEMY_DATABASE_URI = postgresql://dbusername:dbpassword@localhost/dbname
* SQLALCHEMY_TRACK_MODIFICATIONS = True

Note that you'll have to enter your own values for the secret key and the database URI.

After that, run db_create.py to initialize the database tables.

You will also need to set up your Twilio account information as the following environment variables:

* TWILIO_ACCOUNT_SID
* TWILIO_AUTH_TOKEN
* TWILIO_PHONE

If everything is set up properly, you should be able to run 'run.py' and start the service.

##Disclaimer
-----------

I wrote this as a way to familiarize myself with Flask, Twilio, and a number of other things. Instead of spending the time and effort making it into something worth using, I walked away once I had learned what I could. Due to that, I wouldn't recommened attempting to use this in any important situation. 
