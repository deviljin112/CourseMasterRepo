import json
import os
import time


def take_data(data):
    # While loop to continuously take in data from the user
    while True:
        print(
            "Give an input of KEY VALUES.\nYou can provide as many values as you want.\nSubmit each pair with ENTER\nSay 'return' to stop submitting."
        )
        info = input("=> ").split(" ")

        # If the user doesn't say "return" means that we want to add more infromation to the dictionary
        if info[0] == "return":
            break
        # If there is more than 1 element in the list means there is a KEY and VALUE pair
        elif len(info) > 1:
            # First value is KEY
            key = info[0]
            # Other values are VALUE
            values = info[1:]

            # Creates a new position in the dictionary with KEY name
            # Value is set to a joined string of the remaining values provided
            data[key] = " ".join(values)
        else:
            print("That's not a valid input.\nPlease try again!")

    # Returns the newly created dictionary
    return data


# Function for loading a file
def pull_data(file_name):
    with open(file_name, "r") as file:
        data = json.load(file)
    # Returns a dictionary
    return data


# Function for creating / pushing a dictionary into JSON
def constructor(pushed_data, file_name):
    with open(file_name, "w") as data:
        json.dump(pushed_data, data, indent=4, sort_keys=True)


# Function to check if a specific file exists
def check_exists(file_name):
    output = os.path.isfile(file_name)

    if output:
        return "Yes"
    else:
        return "No"


def main():
    # Sets the cached dictionary to empty in case it wasn't before
    stored_data = {}

    # Loops through the menu until user says "exit"
    while True:

        print(
            """
What would you like to do?
Alternatively say 'exit'.

File Management:
    - 'Check' if specific file exists

JSON:
    - 'Create' a file
    - 'Load' a file
    - 'Display' a loaded file
    - 'Clear' cached dictionary

Dictionary:
    - 'Construct' a new dictionary

NOTE: This dictionary is needed to Create a new JSON File"""
        )

        choice = input("=> ")

        if choice.lower() == "exit":
            break
        elif choice.lower() == "check":
            file_name = input("What's the full file name and extension?\n=> ")
            print(check_exists(file_name))
        elif choice.lower() == "create":
            file_name = input(
                "Please provide a full name of a file with the extension.\n=> "
            )

            # Checks for valid name convention i.e. file_name.py
            if "." in file_name:
                # Tries to construct the file
                try:
                    constructor(stored_data, file_name)
                # Catches any errors and prints a simpler message
                except:
                    print(
                        "Error occured!\nCreation of your file failed!\nPlease try again!"
                    )
            else:
                print("That is not a valid file name.\nPlease try again!")
        elif choice.lower() == "load":
            file_name = input(
                "Please provide a full name of a file with the extension.\n=> "
            )
            if "." in file_name:
                try:
                    stored_data = pull_data(file_name)
                except:
                    print("Error occured!\nYour file doesn't exist!\nPlease try again!")
            else:
                print("That is not a valid file name.\nPlease try again!")
        elif choice.lower() == "construct":
            stored_data = take_data(stored_data)
        elif choice.lower() == "display":
            for k, v in stored_data.items():
                print(f"{k}: {v}")
            input("Press ENTER Key To Continue...")
        elif choice.lower() == "clear":
            # In case the user makes an error or would like to make a new action they can clear the cached dictionary
            stored_data = {}
        else:
            print("This option does not exist")

        # Waits for use to read all the infromation before continuing
        time.sleep(3)
        os.system("cls" if os.name == "nt" else "clear")


if __name__ == "__main__":
    print("-=JSON Handler=-")
    main()