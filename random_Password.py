#! python3

# random password generator

# import the random and sys modules. the sys module will be used to exit the program
# at the user's request
import random,sys

# set up the character strings to choose from
alphaLower = 'abcdefghijklmnopqrstuvwxyz'
alphaUpper = alphaLower.upper()
numerals = '0123456789'
spChar = '!@#$%^&*()_+-=[]{};:./<>?'
# NOTE: alternatively you can create lists, e.g. alpha = ['a', 'b', 'c' ... ], but
# since we only need a single character, a string will work just as well

# create a function that chooses a character from a string
# (this also works for lists)
def character(string):
    return string[random.randint(0, len(string) - 1)]

# set up an infinite loop (don't worry, we'll break out of it later)
while True:
    # set up the password variable to accept a string value which will reset each
    # time the loop runs
    password = ''
    
    # make an input loop
    while True:
        # try: and except: is a way of handling exceptions (like value errors)
        # see except ValueError: at the end of this loop to understand what it does
        try: 
            # ask the user for the length of the password and tell the user how
            # to exit the program
            pwLength = int(input('How many characters long? (enter 0 to quit)'))
            if pwLength == 0:
                sys.exit()
            # create a condition that will break the input loop (in this case, it is when
            # the user enters an integer which is a value of 8 or greater)
            if isinstance(pwLength, int) and not pwLength < 8:
                break
            else: # restart the loop if the value is less than 8
                print('The password must be at least 8 characters long.')
                continue
        # tell the loop to restart if the user inputs anything other than an integer
        # (handling the exception)
        except ValueError:
            print('Please enter an integer.')
    
    # create the password loop which will populate the password to the length the user
    # specified
    for i in range(0, pwLength):
        # make a pool of one random character from each type that refreshes each time the loop
        # runs. this will give each type a 25% chance of being chosen
        pool = character(alphaLower) + character(alphaUpper) + character(numerals) + character(spChar)
        # randomly select on of the characters from this pool and add it to the password until 
        # the length is reached
        password += character(pool) # a += b is shorthand for a = a + b
    
    # print the randomly generated password
    print(password)
    # this is the end of the main loop and will start over which will reset the password variable
    # to an empty string
