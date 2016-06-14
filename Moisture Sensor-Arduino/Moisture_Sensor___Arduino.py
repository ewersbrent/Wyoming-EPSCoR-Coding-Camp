# Moisture Sensor - Arduino
# Author: Matt Cook
# Written for Wyoming EPSCoR Summer Coding Camp
# Created May 25, 2016
# Version 1.0

# Added Try block to help with exiting code.  Added annotations and comments.  Inserted valid
# Linux port name.
# Version 0.3 changed to Pymata for Python 2.x due to lack of Raspberry Pi support for Python 3.5 needed for
# PyMata-aio

# Import libraries to interact with Arduino
import sys
import time

from PyMata.pymata import PyMata

# Setup the translator for how we talk to the Arduino
board = PyMata("/dev/rfcomm0", verbose=True)

# Set what "wet" is and store that in a variable
wetVal = 0   # CHANGE ME

# Set which pin(s) we will use to monitor moisture levels
moisturePin = 0

# Make the analog pin 0 tell us what it is observing
board.set_pin_mode(moisturePin, board.INPUT, board.ANALOG)

# Loop through this process
while True:
    # Wait a little so we can see the values a little more clearly.  This way we can see what is happening more easily.
    time.sleep(0.75)

    try:
        # Read moisture sensor values and store it for testing
        moistureLevel = board.analog_read(moisturePin)

        # Test if sensor is wet
        if moistureLevel >= wetVal:
            # Show the user the sensor is wet and how wet it is
            print("The sensor is wet! \nThe moisture level is: " + str(moistureLevel))

    except KeyboardInterrupt():
        # Stop communication with the Arduino and Raspberry Pi
        board.reset()
        sys.exit()

