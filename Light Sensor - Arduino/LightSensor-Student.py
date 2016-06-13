# Light Sensor - Student
# Author: Matt Cook
# Created June 13, 2016
# Written for Wyoming EPSCoR Summer Coding Camp
# Version 1.0

# Incomplete file for handling Light Sensors on the Arduino

# Import necessary library/ies
import sys
from time import sleep
from PyMata.pymata import PyMata

# Setup the way we will communicate with the Arduino using PyMata.
board = PyMata("/dev/rfcomm0")

# Need to give some time to pyFirmata and Arduino to synchronize


lightPin = None

# Enable lightPin to report what it is seeing back to you


# This block allows us to quit the program if we want
# by just pressing some keys on the keyboard
while True:
    try:
        # Read from lightPin

        # wait a little before reading again.
        # NOTE: this makes it easier to detect actual differences


        # Print the values so the user can view them


        # Optional: Set up ranges of light levels.  Make it print messages for
        # each range.


    # If someone enters something, quit the program and end communcation with the Arduino
    except KeyboardInterrupt():
        board.close()
        sys.exit()

