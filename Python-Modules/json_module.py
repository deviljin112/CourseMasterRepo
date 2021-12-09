# Imports JSON Module
import json

# Creates sample dictionary
car_data = {
    "Name": "Tesla",
    "Engine": "Electric",
}

# Writing into a file in JSON format
with open("car_data.json", "w") as data:
    json.dump(car_data, data, indent=4, sort_keys=True)

# Reading a file from a JSON format
with open("car_data.json", "r") as data:
    cars = json.load(data)
