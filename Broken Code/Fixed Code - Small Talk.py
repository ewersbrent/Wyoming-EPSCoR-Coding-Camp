# Fixed Code - Small Talk

# Author: Matt Cook
# Created June 8, 2016
# Written for Wyoming EPSCoR Summer Coding Camp

"""
This code is intentionally broken.  The students are to find and try to
correct the errors as a homework assignment.  The correct code is included in
the Fixed Code directory.
"""


# Define a function to calculate our age based on the user's age
def calcAge (age) :
    return age/2 + 1

# Ask for user's first name
firstName = input("Hi!  What's your name?  ")
                  
# Ask if that's a nickname
isNickname = input("Is that a nickname?  ")
                  
# If not a nickname, respond simply and move on
if isNickname == 'Yes' or isNickname =='yes' :
    print("Oh, ok.")
                  
# Otherwise, ask them what their real name is.
elif isNickname == 'no' or isNickname == 'No' :
        realName = input("Oh, cool!  What's your real name?")
                         
# Ask the user their age
age = input("How old are you, " + firstName)
                         
# If they answer with an absurd number, laugh and respond.
if 150 <= age < 1 :
    print("Haha you're a funny one")
                         
# Otherwise, say you're their age divided by 2 + 1
else :
    # Use our calcAge function to calculate our age and store it
    # it in the ourAge variable.
    ourAge = str(calcAge)
    print("Cool!  I'm " + ourAge)

if not realName == None :
    # Say it was nice meeting the user, and exit.
    print("It was nice meeting you " + firstName + " or should I say " + realName)

else:
    # Say it was nice meeting the user and exit.
    print("It was nice meeting you " + firstName)
                         
