import os
import math, datetime, sys

# Prints CPU's core count
print(os.cpu_count())

# Prints todays date and time
print(datetime.datetime.today())

# Creates a function that returns the path of the file and Python
def current_system_path():
    print("Your current working path")
    return sys.path[0]

path = current_system_path()
print(path)
