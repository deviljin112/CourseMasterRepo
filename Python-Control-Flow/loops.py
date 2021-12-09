################
# Control Flow #
################

# FOR Loop
# Used to iterate through data
# Syntax: for <variable> in <statement>:

## Looping through a list
shopping_list = ["eggs", "milk", "supermalt"]

for item in shopping_list:
    if item == "milk":
        print(item)

## Looping through a dict
sample_dict = {
    "name": "dev",
    "age": 99,
    "course": "DevOps",
    "hobbies": ["Coding", "Gaming", "Sleeping"],
}

# Loops through the key-value pairs in a dictionary
for k, v in sample_dict.items():
    # Checks if the variable 'v' is a list or not
    if isinstance(v, list):
        print(f"Key: {k}")
        # If it is a list, nested for loop to print all the list values
        for i in v:
            print(f"List Value: {i}")
    # Else just print the key and value
    else:
        print(f"Key: {k}, Value: {v}")

# Similar to above but only looping through the keys
for k in sample_dict.keys():
    print(f"Key: {k}")

# Similar to .items() but only looping through the values
for v in sample_dict.values():
    if isinstance(v, list):
        for i in v:
            print(f"List Value: {i}")
    else:
        print(f"Value: {v}")


# WHILE Loop
# Used to loop through a code block until a specific condition is met
# There's a 'break' and 'continue' statement to help control the flow of the loop
# Syntax: while <condition> operator <condition>:

## While looping through a list
sample_list = ["foo", "bar", "dev", "ops"]

# Bool for the while loop
found = False
# While found is False, continue the loop
while not found:
    if "python" in sample_list:
        found = True  # => Can also use "break"
    else:
        sample_list.append("python")

## Adding user input
user_prompt = True
while user_prompt:
    age = input("Please input your age.\n=> ")

    # isdigit() checks if string contains only integers
    if age.isdigit() and int(age) < 100:
        user_prompt = False
    else:
        print("Please provide the age as an Integer")

print(f"Your age is {age}")