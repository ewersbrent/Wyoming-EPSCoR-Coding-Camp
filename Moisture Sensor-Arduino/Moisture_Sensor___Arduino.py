# Moisture Sensor - Arduino
# Author: Matt Cook
# Written for Wyoming EPSCoR Summer Coding Camp
# Created May 25, 2016
# Version 0.2

# Added Try block to help with exiting code.  Added annotations and comments.  Inserted valid
# Linux port name.

# Import libraries to interact with Arduino
from time import sleep
from pymata_aio.pymata3 import PyMata3

# Setup the translator for how we talk to the Arduino
board = PyMata3()

# Set what "wet" is and store that in a variable
wetVal = 0   # CHANGE ME

# Set which pin(s) we will use to monitor moisture levels
moisturePin = 0

# Make the analog pin 0 tell us what it is observing
board.enable_analog_reporting(0)

# Loop through this process
while True:
    # Wait a little so we can see the values a little more clearly.  This way we can see what is happening more easily.
    sleep(0.75)

    try:
        # Read moisture sensor values and store it for testing
        moistureLevel = board.analog_read(moisturePin)

        # Test if sensor is wet
        if moistureLevel >= wetVal:
            # Show the user the sensor is wet and how wet it is
            print("The sensor is wet! \nThe moisture level is: " + str(moistureLevel))

    except KeyboardInterrupt():
        # Stop communication with the Arduino
        board.exit()

