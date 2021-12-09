name = input("Please input your name.\n=> ")
dob = input("Please input your date of birth.\n=> ")
age = int(input("Please input your age.\n=> "))
first_line_addr = input("Please input your first line of the address\n=> ")
house_number = input("Please input your house number\n=> ")
post_code = input("Please input your post code\n=> ")

print(
    f"""
    User Information.
Name: {name}
You were born on: {dob}
Your age is: {age}
Your address is: {first_line_addr}
Your house number is: {house_number}
Your post code is: {post_code}
"""
)

print(
    f"""
    Types of variables.
Name = {type(name)}
Date of birth = {type(dob)}
Age = {type(age)}
Addr = {type(first_line_addr)}
House Num = {type(house_number)}
Post Code = {type(post_code)}
    """
)
