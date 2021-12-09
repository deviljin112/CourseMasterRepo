####################
# Python Operators #
####################

# What are data types and operator

# Boolean => True / False

is_a = True
is_b = False

print(isinstance(is_a, bool))  # => True, is a boolean
print(isinstance(is_b, bool))  # => True, is a boolean

print(is_a == is_b)  # False, they are not equal
print(is_a != is_b)  # True, they are not equal

# Operators

greetings = "Hello World!"

print(greetings.islower())  # => False, characters are not all lowercase
print(greetings.isupper())  # => False, it is not all in uppercase
print(greetings.istitle())  # => True, characters are in title format
print(
    greetings.isalpha()
)  # => False, the string is not in alphabetical order, contains spaces and special character

print(greetings.startswith("H"))  # => True, string does start with `H`
print(greetings.endswith("!"))  # => True, string does end with `!`
print(greetings.startswith("Z"))  # => False, string does not start with `Z`

# None => A nothing value

some_var = None