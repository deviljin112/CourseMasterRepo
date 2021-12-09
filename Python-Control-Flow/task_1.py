import random

# Creates a rating list
ratings = [18, 15, 12, 8, 0]

# Picks a random movie rating
movie_rating = random.choice(ratings)

# Gets user input for age
user_age = int(input("How old are you?\n=> "))

# Check whether the user is old enough for the movie or if the movie is rated "U" for everyone
if user_age >= movie_rating or movie_rating == 0:
    print("You are old enough to watch the movie.\nEnjoy the show!")

# Elif will only be triggered if age is less than rating
# Therefore if the rating is PG it requires a parent
# We check whether the user (who is under the age of 8 => PG) if they with a parent
elif movie_rating == 8:

    # Another input to ask if they with a parent
    parents = input("Did you come with a parent?\n=> ")

    # Checking the answer of the user
    if parents.lower() == "yes":
        print("You can watch the movie!\nEnjoy the show!")
    else:
        print(
            "Sorry you are not old enough to watch this movie!\nYou will need to come back with a parent!"
        )

# In every other case user not allowed to watch the movie
else:
    print("Sorry you are not old enough to watch this movie!")

# Debugging print to see what the rating was choosen at random
print(f"Movie Rating was: {movie_rating}")