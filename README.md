# messaging-system
Combining Flask and Twilio to create a messaging service that will send out messages to a list of contacts.

Installation and Setup
-----------
The version of Python used for this was 3.5, but as far as I know, there weren't any features specific
to 3.5 used, so it may be compatible with some other versions of Python 3. 

Check the requirements.txt for dependencies used.

I used a postgres database while working on this, but I don't think it would be that difficult to tweak
it to use a different database. At any rate, you'll need to create a config.py file in the top directory
(where run.py is) with the following values:
WTF_CSRF_ENABLED = True
SECRET_KEY = 'your secret key goes here'
SQLALCHEMY_DATABASE_URI = postgresql://dbusername:dbpassword@localhost/dbname
SQLALCHEMY_TRACK_MODIFICATIONS = True

Note that you'll have to enter your own values for the secret key and the database URI.

After that, run db_create.py to initialize the database tables.

If everything is set up properly, you should be able to run 'run.py' and start the service.

To-Do
-----------
I originally planned to implement a user privileges system so that certain users could
only access certain pages, but considering there are (I'm assuming) much better programs
out there that do the same thing as this one, it seemed like a waste of time for now.

All of the CSS for this was written by me in order to practice, but I should have
used Bootstrap or another framework to do some of the heavy lifting and make it
look a little better.

Other features I may or may not add in the future:
-ability to import a contact list from a file
-ability to send voice messages
-ability to see contact list and interact with it more intuitively
-user privileges (see above)
-bootstrap (see above)


Changelog
-----------

10/25/2017 - v0.3
Made some minor adjustments, included setup guide in README.
At this point, I'm satisfied with the project and may or may
not work on it anymore.

10/22/2017 - v0.2
Added ability to add and delete contacts, bringing it closer to being useful.

10/15/2017 - v0.1
Base functionality finished, including a login and registration system, a database to handle the data, and a bare-bones messaging system.
