####################
# Python Variables #
####################

import csv

# How can we create a variable

name = "Hubert"  # Declaring a new string variable
age = 23  # Declaring a new int variable
hourly_wage = 5  # Declaring a new int variable
travel_allowance = 2.4  # Declaring a new float variable

# How to find out the type of variable => type()

type(name)  # => String
type(age)  # => Int
type(hourly_wage)  # => Int
type(travel_allowance)  # => Float

# How to take user input

user_input = input("Please enter your name\n=> ")  # Getting user input with a prompt

# How to display data

print(user_input)  # Displays `user_input` in command line

# How to save as csv

with open("names.csv", "w", newline="") as csv_file:
    names_writer = csv.writer(
        csv_file, delimiter=" ", quotechar="|", quoting=csv.QUOTE_MINIMAL
    )
    names_writer.writerow(list(user_input))  # Adds `user_input` in a new row
