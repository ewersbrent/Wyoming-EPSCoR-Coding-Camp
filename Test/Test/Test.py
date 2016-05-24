# Bluetooth Test
# Author Matt Cook
# Created May 23, 2016
# Written for Wyoming EPSCoR Summer Coding Camp

# Version 0.1

from Arduino import Arduino
import pyfirmata
from time import sleep

board = pyfirmata.Arduino('COM3')
sleep(3)

# Using iterator thread to avoid buffer overflow
# If you want to know what this does, follow this link:
# http://pyfirmata.readthedocs.io/en/latest/pyfirmata.html
it = pyfirmata.util.Iterator(board)
it.start()

# define a describing variable so we don't have to type
# a huge amount every time we use this library
ser = Arduino.SoftwareSerial

# Setup virtual serial port using pin 10 to transmit (tx)
# and pin 11 to recieve (rx).  The rate of data transmission
# or baud rate is 9600 bits per second
ser.begin(10, 11, 9600)

# Set pin 13 to make the onboard LED blink
pinLED = board.get_pin("d:13:o")

# send test message to the other device
ser.write("Hello from Arduino!")

# define a function to change LED state
def changeLED(switchLED):
    if(switchLED == 1 or switchLED == 0):
        # Turn LED on or off (0=off 1=on)
        board.digital[pinLED].write(switchLED)
    else:
        # if input is wrong, send error to original sender
        ser.write("wrong input") # TODO: make this print a correct error message
    pass

# Test if a device is connected to our bluetooth. 
if(ser.connected()):

    while(ser.connected()):
        # Read first character sent from the other device, store it in 'a'
        a = ser.read()

        # Send the character to our function to handle
        changeLED(a)



board.exit()
