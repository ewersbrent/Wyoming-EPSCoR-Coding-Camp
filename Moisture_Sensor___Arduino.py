# Moisture Sensor - Arduino
# Author: Matt Cook
# Written for Wyoming EPSCoR Summer Coding Camp
# Created May 25, 2016
# Version 0.1

# Import library to interact with Arduino
import pyfirmata

# Setup the connnection to the Arduino using your computer's
# USB port.  Look in workbook for how to find your port.
port = 'insert port number here'
board = pyfirmata.Arduino(port)

# Use an iterator thread to avoid buffer overflow
# If you want to know what this does, follow this link:
# http://pyfirmata.readthedocs.io/en/latest/pyfirmata.html
it = pyfirmata.util.Iterator(board)
it.start()

# Assign digital pin to read from moisture sensor
moisturePin = board.get_pin('d:11:i')

# Set what "wet" is and store that in a variable
wetVal = 11

# Loop through this process
while True:
    # Read moisture sensor values and store it for testing
    moistureLevel = moisturePin.read()

    # Test if sensor is wet
    if(moistureLevel >= wetVal):
        # Show the user the sensor is wet and how wet it is
       print("The sensor is wet! \nThe moisture level is: " + moistureLevel)

# Stop communication with the Arduino
board.exit()
