#############
# Functions #
#############

# Function
# Syntax: def name(input):

# Creates an example function
def greet():
    print("Hello User")


# This will execute the function
greet()

# Creates an example function with input
# Input is assigned to variable 'who'
def greeting(who):
    print(f"Hello {who}")


# This executes the function and passes a string as an argument
greeting("Dev")


# Create a function that takes in two arguments as ints
# and adds them together
def addition(val_1, val_2):
    return val_1 + val_2


print(addition(2, 2))

# Create a function that takes in two arguments as ints
# and subtracts them from each other
def subtraction(val_1, val_2):
    return val_1 - val_2


print(subtraction(10, 3))
