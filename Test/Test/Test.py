# Bluetooth Test
# Author Matt Cook
# Created May 23, 2016
# Written for Wyoming EPSCoR Summer Coding Camp
# Version 0.2

# EDITS:
# Added support for Software Serial
# Removed pyfirmata from use. Arduino provides buffer overflow protection.

import Arduino
# import pyfirmata
# from time import sleep

board = Arduino.arduino.Arduino(9600,'COM3',2,None)

# Leave in case we
#board = pyfirmata.Arduino('COM3')
#sleep(3)

# Using iterator thread to avoid buffer overflow
# If you want to know what this does, follow this link:
# http://pyfirmata.readthedocs.io/en/latest/pyfirmata.html
# it = pyfirmata.util.Iterator(board)
# it.start()

# We named a variable so it is easier for others to understand
# what is going on.  This is called using a "describing variable".
bluetoothSerial = Arduino.arduino.SoftwareSerial(board)

# Setup "virtual" serial port using pin 10 to transmit (tx)
# and pin 11 to recieve (rx).  The rate of data transmission
# or baud rate is 9600 bits per second.
bluetoothSerial.begin(10,11,9600)

# Set pin 13 to make the onboard LED blink
# pinLED = board.get_pin("d:13:o")
pinLED = board.pinMode(13,"OUTPUT")

# send test message to the other device
bluetoothSerial.write("Hello from Arduino!")

# define a function to change LED state
def changeState(state):

    if state == 1:
        # Turn LED ON (HIGH = ON)
         board.digitalWrite(pinLED,"HIGH")

    elif state == 0:
        # Turn LED OFF (LOW = OFF)
        board.digitalWrite(pinLED,"LOW")

    else:
        # if input is wrong, send error to original sender
        bluetoothSerial.write("wrong input") # TODO: make this print a correct error message

# Test if a device is connected to our bluetooth.
# if bluetoothSerial.connected:

    while True: # bluetoothSerial.connected:
        # Read first character sent from the other device, store it in 'a'
        a = bluetoothSerial.read()

        # Send the character to our function to handle
        changeState(a)



board.close()
