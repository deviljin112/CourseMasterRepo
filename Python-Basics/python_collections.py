######################
# Python Collections #
######################

### Lists ###
# Mutable, remove, add, change
# Syntax: [var, var2, var3]

# Create an example list
shopping_list = ["apple", "milk", "bread"]

# Indexing list items
shopping_list[0]
shopping_list[1]
shopping_list[2]
shopping_list[-1]
shopping_list[1:3]

# Append adds an item at the end of the list
shopping_list.append("eggs")

# Inserts an item in a specific index
shopping_list.insert(0, "chicken")

# Removes the first occurance of the item in a list
shopping_list.remove("milk")

# Pops a specific index from the list
# Pop stores the poped value in a variable if set
shopping_list.pop(0)

# Replacing an object
shopping_list[1] = "beef"

# Clear the list i.e. remove all items in the list
shopping_list.clear()


### Tupels ###
# Immutable, cannot be changed
# Syntax: (var1, var2, var3)

# Create an example tuple
short_list = "paracetamol", "xanax", "vitamin-c", "eggs", "bread"

# short_list[0] = "hello"
# Error item does not support assignment
short_list[0]  # => paracetamol


### Dictionaries ###
# Mutable, add, remove, pop, alter
# Only one unique key allowed
# Syntax: {key: value}

# Create example dictionary
some_dict = {"key": "value", "name": "hubert", "foo": "bar"}

# Accessing a key / value
some_dict["key"]  # => value
some_dict.get("key")  # => value

# Accessing only the keys
some_dict.keys()

# Accessing only the values
some_dict.values()

# Accessing all the pairs as tuples
some_dict.items()

# Changing a value
some_dict["name"] = "Dev"

# Add new key to dictionary
some_dict["gender"] = "male"

# Removes the specified key
# Returns the value when assigned to a variable
some_dict.pop("key")
del some_dict["name"]

# Clear all key-value pairs
some_dict.clear()

## TASK ##
example_dict = {
    "key": "value",
    "name": "james",
    "lessons": 4,
    "lesson_names": ["operators", "data types", "variables"],
}

# Accessing a list within a dictionary
example_dict["lesson_names"][1]  # => data types


## TASK 2 ##
user_details = {
    "first_name": "Hubert",
    "last_name": "Dev",
    "dob": "01/01/2001",
    "address": "100 Some Road",
    "course": "DevOps",
    "grades": ["A", "A", "B"],
    "hobbies": ["skating", "gaming", "coding"],
}

# Adding an item to "hobbies" list
user_details["hobbies"].append("sleeping")

# Removing an item from "hobbies" list
user_details["hobbies"].remove("gaming")

print(user_details["hobbies"])
