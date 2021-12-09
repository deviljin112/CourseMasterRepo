# Create a variable to store a file data using open()


## Iteration 1
try:
    some_file = open("orders.text")
except:
    print("There was an error!")


## Iteration 2
# Use try block when we know there might be an error
try:
    file_data = open("orders.text")  # => Error

# Catch the specific error and print a custom message
except FileNotFoundError as error_msg:  # Alias the error message to a variable
    print(f"File does not exist!\n{error_msg}")

# If there is no error do something with that variable
else:
    print(file_data)

# Regardless of the above result, always run this block at the end
finally:
    print("End of function")
