# Author: Matt Cook
# Created May 19, 2016
# Written for Wyoming EPSCoR Summer Coding Camp 2016
# Verson 1.0


# import the required libraries
from time import sleep

import pyfirmata


# The documentation for each library is found here
# http://pyfirmata.readthedocs.io/en/latest/pyfirmata.html
# https://docs.python.org/2/library/time.html


# define custom function to perform Blink action
def blinkLED(pin, repeat):
    # While loop blinks the LED as many times as the
    # user specified.  
    while (repeat > 0):
        # Turn the LED on
        board.digital[pin].write(1)
        # Wait 1 second
        sleep(1)
        # Turn the LED off
        board.digital[pin].write(0)
        # Wait 1 second
        sleep(1)
        print(repeat)
        # Decrement (reduce) repeat by 1
        repeat = repeat - 1
    pass

# Associate the port and board with the pyFirmata protocol
# Change your port to the one your Raspberry Pi uses
# *Look in your workbook to find out how*
port = 'COM3'
board = pyfirmata.Arduino(port)

# Need to give some time to pyFirmata and Arduino to synchronize
sleep(5)

# Using iterator thread to avoid buffer overflow
# If you want to know what this does, follow this link:
# http://pyfirmata.readthedocs.io/en/latest/pyfirmata.html
it = pyfirmata.util.Iterator(board)
it.start()

# Assign digital pin 7 to myLED.
myLED = 7
    
# Ask for input from user and save their answer in a variable
numOfBlinks = input("How many times do you want to blink the LED? (0-20)")

# Send the user's decision to your blinkLED function
blinkLED(myLED, numOfBlinks)

# Release the board from your control when the user is done    
board.exit()
