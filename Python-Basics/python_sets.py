###############
# Python Sets #
###############

# Set
# Mutable, add, update, remove
# Unindexed, unordered, unique items
# Syntax: {var1, var2}

# Create example sets
car_parts = {"Wheels", "Doors", "Radio"}

# Display all items in a set
print(car_parts)

for v in car_parts:
    print(v)

# Adding an item
car_parts.add("Engine")

# Adding multiple items
car_parts.update(["Seat", "Seat Belt", "Steering Wheel"])

# Removing an item
# If the item doesn't exist it will raise an error
car_parts.remove("Radio")

# Remove a specific item
# If the item doesn't exist it will NOT raise an error
car_parts.discard("Radio")

# Removing last item
# Remember last item is unknown
car_parts.pop()

# Checking if an item exists in a set
print("Radio" in car_parts)  # => False
