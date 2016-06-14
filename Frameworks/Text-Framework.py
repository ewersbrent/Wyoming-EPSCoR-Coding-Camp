# Text - Framework
# Author: Matt Cook
# Created June 14, 2016
# Written for Wyoming EPSCoR Summer Coding Camp
# Version 1.0


"""
In this file we are sending a text message to our selves using email.  The email is converted
by TextBelt into an SMS format (the format of a regular text message without emojis).  The SMS
is then sent to your phone.  We can only text this number 3 times an hour, so make sure you only
use the texts to alert you of major events.
"""

# The PycURL library we are using is just a way for us to use a prewritten program for handling
# Internet based communication.  The underlying program is called cURL.  If you want to learn more
# about how it works, look here http://www.angryobjects.com/2011/10/15/http-with-python-pycurl-by-example/
import pycurl

# This line opens an object to deal with HTTP communication for us. 'text' is now the
# object we will be working with.
text = pycurl.Curl()

# This sets the 'text' variable to deal with our textbelt website.
text.setopt(text.URL, 'http://textbelt.com/text')

# Change this to be the message you want to send.
message = 'our message'

# This sets up the message we want to send.  POST is a way of sending information
# and asking for a response about what happened to the information we sent.  Hopefully,
# we should get something like {success:true}
# NOTE: Replace the number after 'number=' with the phone number you want to text.
text.setopt(text.POSTFIELDS, 'number=1234567890&message=' + message)

# This actually performs our POST operation from before.
text.perform()

# This gets rid of our object we were working with.
text.close()

