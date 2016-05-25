# Bluetooth - Arduino
# Author: Matt Cook
# Created May 25, 2016
# Written for Wyoming EPSCoR Summer Coding Camp
# Version 0.1

import serial
import pyfirmata
from time import sleep

# Open a serial port with pyfirmata to upload the program
port = 'COM3'
board = pyfirmata.Arduino(port)
# FOR USER: Once the program is uploaded, disconnect the USB cable

# Wait for the cable to disconnect.  Test connection every second
while( board.taken() == True):
    sleep(1)

# Once disconnected, continue

# Open a serial port for Bluetooth communication
btSerial = serial.Serial(baudrate=9600)

# Read a single character from the Bluetooth connection
rasPi = btSerial.read()

# Test for which input was given
# Do stuff with regards to the input



