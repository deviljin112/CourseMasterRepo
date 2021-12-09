# Import datetime module for operations on date and time
import datetime

# Take in inputs from the user about their name, age and birthday
name = input("What's your name stranger?\n=> ").capitalize()
age = int(input("How old are you?\n=> "))

# This retrives the input and splits it as a space
# It uses multiple variable assignment instead of creating a list
# It is assumed that the user will follow the formatting an only two values will be given
day, month = input("When is your birthday?\nFormat: DD MM\n=> ").split(" ")

# Because they are dates we want to change the strings into integers
day, month = int(day), int(month)

# Get the current date
today = datetime.datetime.now()

# Find out the year user was born
user_year = today.year - age

# Format a datetime instance of users dob
birthday = datetime.datetime(user_year, month, day)

# Create a bool to track whether a user had birthday or not
had_birthday = True

# Get the value of days until the birthday
# (positive means its after today's day, negative means its before today's day)
# Day being positive or negative does not mean that the birthday occured
# As birthday may be on 1st of October but today its 21st of March therefore "days_left" will be -20
# This difference is the amount of days until the actual birthday
days_left = today.day - day

# Check whether the user had their birthday or not
if today.month - month < 0:
    # Get the amount of months until birthday into a variable
    months_left = month - today.month

    # Set the bool to false as the user didn't have their birthday yet
    had_birthday = False

    # If days left is negative, make it a positive value for clarity
    if days_left < 0:
        days_left *= -1

# If the birthday is this month, and days left is not negative (i.e. the birthday didnt happen yet)
elif today.month == month and days_left < 0:

    # Months left is 0 as its this month
    months_left = 0

    # Set days left to positive as before
    days_left *= -1

    # Set the bool to false like before
    had_birthday = False

# Find out the difference in deltatime between today and dob
difference = today - birthday

# Find out how many hours, minutes and seconds has elapsed since user's birth
hours_in_days = difference.days * 24
hours = (difference.seconds // 3600) + hours_in_days
minutes = (difference.seconds // 60) % 60
seconds = int(difference.seconds % 60)

# Print out all the main information about the user
print(
    f"""
OMG {name}!
You are {age},
So, you were born on {birthday.strftime("%d %b %Y")}.
You've been around for
{hours} hours,
{minutes} minutes,
{seconds} seconds.
"""
)

# Birthday specific print
# This print depends whether the user had their birthday or not
if not had_birthday:
    print(f"You have {days_left} days and {months_left} months until your birthday!")
else:
    print(f"You already had your birthday :(\nWell... Happy late Birthday!")