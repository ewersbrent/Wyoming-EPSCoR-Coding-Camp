# PyMata Bluetooth
# Author Matt Cook
# Created May 31, 2016
# Written for Wyoming EPSCoR Summer Coding Camp
# Version 0.1

# Attempting Bluetooth Communication with SoftwareSerial Library



# import necessary libraries
import serial
import pyfirmata
from time import sleep

# Setup how we view the Arduino.  This is necessary because there
# are multiple styles of Arduinos out there.  We need to make sure
# we are using the right board (Arduino = Arduino Uno).
board = pyfirmata.Arduino('COM3')

# Wait for the two machines to synchronize
sleep(3)

def blinkLED():


# TO DO: Make this work and simplify
#
# # Define a function to make the user's input into something
# # the Arduino can understand.
# def askArduino(instruction, pin, pinType):
#     # board.get_pin changes the way a certain pin behaves.  The input is usually like this:
#     # 'a:4:o' for "set analog pin 4 to output what we send" or 'd:10:i' "set digital pin 10 to provide us with input"
#     setPin = board.get_pin(pinType + ':' + pin + ':' + instruction)
#
#     # Wait a half second before reading from the buffer
#     # this will prevent reading before the transmission is done
#     board.pass_time(0.5)
#
#     # Read from the Arduino and send the information back to the user
#     # TO DO: have makeReadable() parse the information recieved into human-
#     # readable output
#     return   # makeReadable()
#
# # TO DO: Define a function to make the input from the Arduino into
# # something we want to see.
# def makeReadable():
#     # Read from the Arduino until we are ready
#     # NOTE: the second number is how much data is waiting for us sent from the Arduino.
#     # This is an example of how we can use buffers to save data for us until we want it
#     return board
#     # TO DO: Make the output human readable/useful
#
#
# # Start a loop to ask the user how they want the Arduino to act.
# # Option 1: We ask the Arduino for a reading when we want.
# while True:
#
#
#     # This is called a "Try Block".  This structure allows us to stop the
#     # program without unplugging everything.
#     try:
#             # The "while not" statements here double check the option selected will work.  They do what is called
#             # input validation.  This is important to do for two reasons. The first, it makes the program easier for
#             # the user to work with.  The second, it makes it harder for the user to "break" your program.  It's a
#             # win-win for you and the user.
#
#             instruction = input("What do you want the Arduino to do? 'i' will get your info from the pin, 'o' will "
#                                 "send information to the pin")
#
#             while not instruction=='i' or not instruction=='o' :
#                 instruction = input("Please enter a valid instruction. 'i' will get your info from the pin, 'o' will "
#                                     "send information to the pin")
#
#             # str.lower() makes the user's input into all lower case letters.  This makes it easier for us to double
#             # check if the user chose an option we can work with. Otherwise, we would have to check for all possible
#             # ways the user could enter the word. Examples: Analog, analog, aNalog, digital, digiTal, Digital
#
#             pinType = str.lower( input("Is the pin Analog or Digital?") )
#
#             while not pinType == 'analog' or not pinType == 'digital' :
#                 pinType = str.lower( input("Please enter a valid option. Is the pin Analog or Digital?") )
#
#             # int() makes the input into an integer.  Once again, it makes our lives easier when double checking
#             # what the user asked us to do.
#             pin = int( input("Which pin do you want to use?") )
#
#             while not pin <=13 and pin>=1:
#                 pin = int( input("Valid pins are whole numbers between 1 and 13. Which pin do you want to use?") )
#
#             # Now we send our validated input to a function that will do a certain task (send instructions to the
#             # Arduino and )
#             askArduino(instruction, pin, 0)
#             # Prints the results of our makeReadable function
#             print (makeReadable())
#
#     except:
#         # The user pressed the keys to quit (ctrl+C)
#         KeyboardInterrupt()
#         # Stop our connections so we don't waste resources
#         board.exit()
#
# # Option 2: We keep communication with the Arduino open.  The Arduino
# # will report what it observes at set intervals (to save battery and
# # prevent buffer overflow).
# while True:
#     # This is called a "Try Block".  This structure allows us to stop the
#     # program without unplugging everything.
#     try:
#         if
#             # Prints the results of our makeReadable function
#             print (makeReadable())
#
#     except:
#         # The user pressed the keys to quit (ctrl+C)
#         KeyboardInterrupt()
#         # Stop our connections so we don't waste resources
#         board.exit()
