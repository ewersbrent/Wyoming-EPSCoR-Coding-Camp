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

# The urllib library we are using is just a way for us to use a prewritten program for handling
# Internet based communication.  The underlying program is called cURL.  If you want to learn more
# about how it works, look here https://docs.python.org/2/library/urllib.html#examples
import urllib

# This line specifies which website we will be interacting with during the
# email-to-text conversion
address = 'http://textbelt.com/text'

# We need to make things easier to read, so we store our message in this describing variable
# before we send it off.
message = 12345

# This line creates our message and makes sure we are using only standard characters because
# web transmissions can be picky about special characters
info=urllib.urlencode({'number':'3031234567','message':message})

# This line sets up the way we want to send and receive information to/from the
# website.  It also sends our POST (let us send something and send us a response) request.
post = urllib.urlopen(address,info)

# This prints the result of our website interaction.  It tells us if the message was
# sent successfully or failed to send.
print post.read()

