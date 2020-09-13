#! python3

# random password generator

import random,sys

# first we will need to create the appropriate variables that contain the four character types:
# lowercase letters, uppercase letters, numerals, and special characters
alphaLower = 'abcdefghijklmnopqrstuvwxyz'
alphaUpper = alphaLower.upper()
numerals = '0123456789'
spChar = '!@#$%^&*()_+-=[]{};:./<>?'

pool = alphaLower + alphaUpper + numerals + spChar

# second create a function which will chose a character from a string
def character():
    return pool[random.randint(0, len(pool) - 1)]

# third, start an infinit loop
while True:
    # fourth, prep the password variable to expect a string
    password = ''
    
    # fifth, start another loop to handle the input
    while True:
        try:
            pwLength = int(input('How many characters long? (enter 0 to quit)'))
            if pwLength == 0:
                sys.exit()
            if pwLength > 0:
                break
        except ValueError:
            print('Please enter an integer.')
    
    password += character()
    print(password)
    
