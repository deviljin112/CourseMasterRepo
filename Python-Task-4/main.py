user_details = {
    "first_name": "Hubert",
    "last_name": "Dev",
    "dob": "01/01/2001",
    "address": "100 Some Road",
    "course": "DevOps",
    "grades": ["A", "A", "B"],
    "hobbies": ["skating", "gaming", "coding"],
}

del user_details["grades"]
user_details["age"] = 20
user_details["course"] = "Business Management"

for v in user_details.values():
    print(type(v))

print(user_details["hobbies"][::-1])
