import requests


def main():
    arg = input("Please enter your PostCode.\nOr say 'random'.\n=> ")

    if arg == "random":
        link = "http://api.postcodes.io/random/postcodes"
    else:
        link = f"http://api.postcodes.io/postcodes/{arg}"

    r = requests.get(link)
    status = r.status_code
    r_json = r.json()

    if status == requests.codes.ok:
        # Prints all results from the JSON table
        for k, v in r_json["result"].items():
            print(f"{k.capitalize()}: {v}")

    else:
        print(r_json["error"])


if __name__ == "__main__":
    main()