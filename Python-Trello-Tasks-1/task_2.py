# Create a loop that wil re-occur 10 times
# Uses "_" as the actual return value of the range function is irrelevant
for _ in range(10):
    print("Hello!")

# Creates an empty list ready for new data to be added
list_names = []

# Similarly to before loop will re-occur 5 times
for _ in range(5):

    # Instead of creating seperate variable for the input
    # It is instantly added to the list
    # Input will be overriden on each loop anyway
    # therefore doesnt need to be stored in memory
    list_names.append(input("Please input a name\n=> "))

print(list_names)

# Creates another empty list
list_name_lower = []

# Loop over each value in the `list_names` list
for v in list_names:

    # Add the lowercase version of the value from the iterated list
    list_name_lower.append(v.lower())

print(list_name_lower)

# Creates another empty list
even_strings = []

# Loop over each value in the `list_name_lower` list
for i in list_name_lower:

    # Checks the length of the string
    # Checks whether the number is divisible by 2
    # If it is then it must be even
    if len(i) % 2 == 0:

        # Even strings are added to an empty list
        even_strings.append(i)

print(even_strings)