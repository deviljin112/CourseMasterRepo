# First we take in a string of the trainee's first, middle and last name and capitalise() the first letter in case they have only used lower-case
first_name = input("Please input your first name.\n=> ").capitalize()
middle_name = input("Please input your middle name.\n=> ").capitalize()
last_name = input("Please input your last name.\n=> ").capitalize()

# We then take in the first line of trainee's address and use title() so that every first letter in a word is capitalised
addr = input(
    "Please input the first line of your address.\n(Format: 111 Road Name)\n=> "
).title()

# Followed by their post code, here all the letters are capitalised with upper()
post_code = input("Please input your post code.(Format: AA11 2BB\n=> ").upper()

# We then ask for the trainee's national insurance number which we also full capitalise like previously with upper()
ni_num = input(
    "Please input your National Insurance Number.\n(Format: AA123456B)\n=> "
).upper()

# We also ask for course name, as this can be a multiple words like "Business Management" we use title() to capitalise every first letter in the word
course = input("Please input the course you've applied to.\n=> ").title()

# Lastly, we find out their most recent education level and capitalise the first letter as this is most likely a single word
education = input("Please input your most recent education level.\n=> ").capitalize()

# We then print all this information back to the user using ''' also known as a multi line string
# This combined with the 'f' allows us for easy formatting of variables inside of the string
# National Insurance Number has custom formatting using string slicing
# This makes the national insurance number look like this: AA-123456-B
print(
    f"""User Details:
Your full name is {first_name} {middle_name} {last_name}.
You live at
{addr},
{post_code}.
Your National Insurance number is {ni_num[0:2]}-{ni_num[2:8]}-{ni_num[8:]}.
You have applied to a {course} course.
Your most recent education level is {education}
"""
)
