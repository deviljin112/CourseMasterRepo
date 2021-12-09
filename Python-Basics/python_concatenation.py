########################
# Python Concatination #
########################

# What is concatination
first_name = "James"
middle_name = "007"
last_name = "Bond"

print(first_name, middle_name, last_name)  # => James 007 Bond

age = 56

print(first_name, middle_name, last_name, age)  # => James 007 Bond 56

# Casting int to string
print("Age " + str(age))  # => Age: 56

# Casting string to int
print(int(middle_name))  # => 7

# Concatinating Variables
name = input("Please input your name\n=> ")
print(f"Hello {name}")

# Declaring strings with double or single quote
quotes = "double quotes 'wow'"

# String slicing
# Indexing a position returns the value in that position, usage [<index>]
greetings = "Hello World!"
print(greetings[0:5])  # => "Hello", returns from 1st to 4th character

# Stripping a string
# Strip() Removes specified character at the end of the string
white_spaces = "Lot's of spaces at the end               "
print(len(white_spaces))  # => 41
print(white_spaces.strip(" "))
print(len(white_spaces.strip(" ")))  # => 26

# Counting string
# Count() returns the number of occurances of a specified string
example_text = "Lots of different text, text text also some other text"
print(example_text.count("text"))  # => 4

# Replace a string
print(example_text.replace(",", "!"))
# => "Lots of different text! text text also some other text"

# Capitalise, Upper, Lower, Title
text_example = "new Text exaMPLE"
print(text_example.capitalize())  # => "New text example"
print(text_example.upper())  # => "NEW TEXT EXAMPLE"
print(text_example.lower())  # => "new text example"
print(text_example.title())  # => "New Text Example"
