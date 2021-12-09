# This is the main file that imports other files
from python import Python


def main():
    # Create an instance of the Python Class
    shnake = Python()

    # Print out some of the attributes from the Class and its Parents
    print(f"Alive: {shnake.alive}")
    print(f"Cold Blooded: {shnake.cold_blooded}")
    print(f"Venom: {shnake.venom}")
    print(f"Two Lungs: {shnake.two_lungs}")


# Using __name__ and __main__
# Syntax: if __name__ == "__main__":
if __name__ == "__main__":

    # print(f"This is the name of the file '{__name__}'")  # => __main__
    main()