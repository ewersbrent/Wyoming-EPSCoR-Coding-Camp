# Light Sensor - Arduino
# Author: Matt Cook
# Created May 25, 2016
# Written for Wyoming EPSCoR Summer Coding Camp
# Version 0.1

# Import necessary library/ies
from time import sleep

import pyfirmata

# Associate the port and board with the pyFirmata protocol
# Change your port to the one your Raspberry Pi uses
# *Look in your workbook to find out how*
port = 'COM3'
board = pyfirmata.Arduino(port)

# Need to give some time to pyFirmata and Arduino to synchronize
sleep(2)

# Using iterator thread to avoid buffer overflow
# If you want to know what this does, follow this link:
# http://pyfirmata.readthedocs.io/en/latest/pyfirmata.html
it = pyfirmata.util.Iterator(board)
it.start()

# Set up the pin we will use to monitor the photocell
lightPin = board.get_pin('a:7:i')

# This block allows us to quit the program if we want
# by just pressing some keys on the keyboard
try:
    while True:
        # Start reading the values from the photocell
        # Print the values so the user can view them
        print("Light Level: " + lightPin.read())

        # Optional: Set up ranges of light levels.  Make it print messages for
        # each range. Hint: if we do this we need a way to 
        low = 1
        medium = 2
        high = 3
        if('between this and that'):
            print("words")
        elif('between that and that'):
            print("more words")
        elif("greater than that"):
            print("even more words")

# If someone enters something, quit the program
except KeyboardInterrupt:
    board.exit()

