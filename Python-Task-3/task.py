# Create an example list
item_list = ["Shoe", 2, "Deer", 10.7, 912842, "Skittles", "Batman"]

# Print the length of the list
print(len(item_list))  # => 7

# Create a for loop to iterate over each item and check the type
for k in item_list:
    print(type(k))
# String, Int, String, Float, Int, String, String

item_list.append("Phone")
print(item_list)
# Shoe, 2, Deer, 10.7, 912842, Skittles, Batman, Phone

item_list.remove("Deer")
print(item_list)
# Shoe, 2, 10.7, 912842, Skittles, Batman, Phone

item_list[3] = 313
print(item_list)
# Shoe, 2, 10.7, 313, Skittles, Batman, Phone

item_list.pop(0)
print(item_list)
# 2, 10.7, 313, Skittles, Batman, Phone

print(item_list[::-1])
# Phone, Batman, Skittles, 313, 10.7, 2