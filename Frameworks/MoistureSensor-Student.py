# Moisture Sensor - Student
# Author: Matt Cook
# Written for Wyoming EPSCoR Summer Coding Camp
# Created May 25, 2016
# Version 1.0

# Incomplete file for handling the Moisture Sensor on the Arduino

# Import libraries to interact with Arduino
import sys

from PyMata.pymata import PyMata
# Setup the translator for how we talk to the Arduino
board = PyMata("/dev/rfcomm0", verbose=True)

# Set what "wet" is and store that in a variable


# Set which pin we will use to monitor moisture levels


# Enable the analog pin of our choice to report what it is observing


# Loop through this process
while True:
    # Wait a little so we can see the values a little more clearly.  This way we can see what is happening more easily.


    try:
        # Read moisture sensor values and store it in a variable for later


        # Test if sensor is wet

            # Show the user the sensor is wet and how wet it is


    except KeyboardInterrupt():
        # Stop communication with the Arduino and Raspberry Pi
        board.reset()
        sys.exit()

