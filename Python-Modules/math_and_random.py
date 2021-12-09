# Task
# get user input of a float number
# check if the number is lower than .50 then round the figure to lower end
# check if the number is greater than .51 then round the figure to higher end
# example - num_float = 23.66 - round it to 24, num_float = 23.50 - round it to lower end

# Imports a module
import math
import random

# If the input is not the right format, catch the error
try:
    # Takes a float input
    number = float(input("Input a Float Number.\n=> "))
except:
    # If error, print a message
    print("That is not a float value!")
else:
    # If no error occured perform the action
    print(f"Starting number: {number}")

    # number % 1 will result in returning all the numbers after the decimal point
    if number % 1 < .5:
        output = math.floor(number)
    else:
        output = math.ceil(number)

    print(f"Formatted number: {output}")
