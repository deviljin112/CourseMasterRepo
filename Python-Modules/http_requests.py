# Imports http requests module
import requests

# Imports emoji module
import emoji

# Makes a request to a website
r = requests.get("https://www.bbc.co.uk")

## First Iteration

# If the website is running (code = 200)
if r.status_code == 200:
    # Emojize is emoji module's way of turning text into an emoji
    print(emoji.emojize("Website is Live! :thumbs_up:"))
elif r.status_code == 404:
    print(emoji.emojize("Website is unavailable :sad_face:"))
# In any other case
else:
    print(emoji.emojize("Website is dead... :thumbs_down:"))


## Second Iteration
def check_response_code():
    if r.status_code == 200:
        print(emoji.emojize("Website is Live! :thumbs_up:"))
    elif r.status_code == 404:
        print(emoji.emojize("Website is unavailable :sad_face:"))
    else:
        print(emoji.emojize("Website is dead... :thumbs_down:"))


## Third Iteration
def bool_response_code():
    if r.status_code == requests.codes.ok:  # => True
        print(emoji.emojize("Website is Live! :thumbs_up:"))
    elif r.status_code == requests.codes.not_found:  # => False
        print(emoji.emojize("Website is unavailable :sad_face:"))
    else:
        print(emoji.emojize("Website is dead... :thumbs_down:"))
