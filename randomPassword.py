#! python3

# random password generator (using strings)

# import the random module
import random

# create the four variables which will contain the strings of the 
# four character types: uppercase letters, lowercase letters,
# digits, and special characters
alphaLower = 'abcdefghijklmnopqrstuvwxyz'
alphaUpper = alphaLower.upper()
num = '0123456789'
spChar = '!@#$%^&*()_+-=[]{};:./<>?'

# create a pool of everything from which to select a random character
pool = alphaLower + alphaUpper + num + spChar

# create a function that will select a random character from the pool
def randomChar():
    return pool[random.randint(0, len(pool) - 1)]

# create an infinite loop (don't worry, we'll break out of it later)
while True:

    # tell the script how to handle an exception. In this case it will 
    # be ValueError
	try:
		
        # ask the user for the password length they want. because we want this
        # to be an integer, we told the script to check the user input. if it is
        # not an integer, the loop will restart
        pwLength = int(input('How many characters long? '))
	
        # set up the password variable to hold a string
        password = ''
		
        # create a loop that will run as many times as the number given by
        # by the user. each loop will add one more character until the loop 
        # reaches the same value as pwLength
        for i in range(0, pwLength):
		
            # reassign the variable to add the special character to the previous
            # result
            password += randomChar() # this is the same as password = password + randomChar()
			
        # print the final result when the loop finishes
        print(password)
		
        # break the infinite loop. This will only work if pwLength is an integer
        break
		
    except ValueError:
        # This is where the script handles the exception
        print('Please provide an integer.')
