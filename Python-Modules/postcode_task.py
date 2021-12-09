import requests


def main():
    arg = input("Please enter your PostCode.\nOr say 'random'.\n=> ")

    # Switch if statement for random postcode option
    if arg == "random":
        link = "http://api.postcodes.io/random/postcodes"
    else:
        link = f"http://api.postcodes.io/postcodes/{arg}"

    # Makes a GET Request from the link
    r = requests.get(link)
    # Assigns the status code to an variable
    status = r.status_code
    # ASsigns the JSON return value to a variable
    r_json = r.json()

    # List of all the arguments that we need for printing
    display_info = ["postcode", "longitude", "latitude"]

    # If status_code == 200
    if status == requests.codes.ok:
        # Only display the information in the list
        for i in display_info:
            print(f"{i.capitalize()}: {r_json['result'][i]}")
    else:
        # If status code is anything other than 200 print the error
        print(r_json["error"])


if __name__ == "__main__":
    main()