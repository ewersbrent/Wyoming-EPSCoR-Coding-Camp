# New Bluetooth
# Author Matt Cook
# Created May 31, 2016
# Written for Wyoming EPSCoR Summer Coding Camp
# Version 0.1

# Attempting Bluetooth Communication with Arduino-Serial library

# Import necessary libraries
import serial
import pyfirmata
from time import sleep

# Setup how we view the Arduino.  This is necessary because there
# are multiple styles of Arduinos out there.  We need to make sure
# we are using the right board (Arduino = Arduino Uno).
board = pyfirmata.Arduino()

# Open serial port to communicate with the Arduino
# We shouldn't need to use Software Serial because we are
# powering the Arduino with a battery, but we may have to.
# NOTE: CHANGE THE PORT NUMBER IF YOU NEED TO
connection = serial.Serial('/dev/ttyAMA0', 9600)

# Wait for the two machines to synchronize
sleep(3)


# Define a function to make the user input into something
# the Arduino can understand.
def instructArduino(instruction):
    # Make sure the input can be read by the Arduino
    toArduino = int(instruction)
    # Double check if connection is available
    if connection.isOpen():
        # Sends the instruction to the Arduino over our connection
        connection.write(toArduino)
    else:
        # We use double quotes (") here so we can use an apostrophe (') in "isn't"
        print("The Arduino isn't connected...")


# Define a function to make the input from the Arduino into
# something we want to see.
def readArduino():
    # Read from the Arduino until we are ready
    # NOTE: the second number is how much data is waiting for us sent from the Arduino.
    # This is an example of how we can use buffers to save data for us until we want it
    return connection.read(connection, connection.in_waiting())
    # TO DO: Make the output human readable/useful


# Start a loop to ask the user how they want the Arduino to act.
# Option 1: We ask the Arduino for a reading when we want.
while True:


    # This is called a "Try Block".  This structure allows us to stop the
    # program without unplugging everything.
    try:
        if connection.is_open():
            instruction = input("What do you want from the Arduino?")
            instructArduino(instruction)
            # Prints the results of our readArduino function
            print (readArduino())

    except:
        # The user pressed the keys to quit (ctrl+C)
        KeyboardInterrupt()
        # Stop our connections so we don't waste resources
        board.exit()
        connection.close()

# Option 2: We keep communication with the Arduino open.  The Arduino
# will report what it observes at set intervals (to save battery and
# prevent buffer overflow).
while True:
    # This is called a "Try Block".  This structure allows us to stop the
    # program without unplugging everything.

    try:
        # Wait half a second to read again
        sleep(0.5)
        if connection.is_open():
            # Prints the results of our readArduino function
            print (readArduino())
            # TO DO: If we want to only print when certain conditions are met
            # a different function will need to be written

    except:
        # The user pressed the keys to quit (ctrl+C)
        KeyboardInterrupt()
        # Stop our connections so we don't waste resources
        board.exit()
        connection.close()