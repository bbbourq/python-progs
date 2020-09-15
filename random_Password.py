#! python3

# random password generator

import random,sys

# first we will need to create the appropriate variables that contain the four character types:
# lowercase letters, uppercase letters, numerals, and special characters
alphaLower = 'abcdefghijklmnopqrstuvwxyz'
alphaUpper = alphaLower.upper()
numerals = '0123456789'
spChar = '!@#$%^&*()_+-=[]{};:./<>?'

# second create a function which will chose a character from a string
def character(pool):
    return pool[random.randint(0, len(pool) - 1)]

# third, start an infinite loop
while True:
    # fourth, prep the password variable to expect a string
    password = ''
    
    # fifth, start another loop to handle the input
    while True:
        try:
            pwLength = int(input('How many characters long? (enter 0 to quit)'))
            if pwLength == 0:
                sys.exit()
            if isinstance(pwLength, int) and not pwLength < 8:
                break
            else:
                print('The password must be at least 8 characters long.')
                continue
        except ValueError:
            print('Please enter an integer.')
        
        for i in range(0, pwLength):
            pool = character(alphaLower) + character(alphaUpper) + character(numerals) + character(spChar)
            password += character(pool)
        
        print(password)
