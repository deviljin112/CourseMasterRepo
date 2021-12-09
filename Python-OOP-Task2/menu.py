# Creates parent class
class Menu:
    # Initialises the parent class
    def __init__(self):
        # Only variable in this class is the Menu
        self.menu = [
            "Spicy Chicken",
            "Sweat and Sour Beef",
            "Fries",
            "Mash Potatoes",
            "Pizza",
            "Carbonara",
            "Bolognese",
            "Wine",
            "Beer",
            "Water",
            "BLT Sandwich",
        ]


# Creates a child class of parent "Menu"
class Waiter(Menu):
    def __init__(self):
        # Imports the variables from parent
        super().__init__()
        # Creates a new child-specific variable
        self.order = []

    # Class function for ordering from the menu
    def ordering(self):
        # First iteration prompt
        print("What would you like to order?")

        # Boolean for looping
        is_ordering = True

        while is_ordering:
            # Takes input
            choice = input("=> ")

            # Checks that this item is available in the menu
            if choice in self.menu:
                # If yes then adds to the order
                self.order.append(choice)
            else:
                print("We do not offer that type of food")

            print("Anything else?")

            # Asks user if they would like to add more items
            choice_2 = input("=> ")
            if choice_2.lower() == "no":
                # If no, breaks the loop
                is_ordering = False
            else:
                print("What else would you like?")

        return self.order

    # This is used for clean formatting when showing the self.order table
    def __str__(self):
        return " ".join(k for k in self.order)


def main():
    user = Waiter()

    print("Welcome to our restaurant.")
    user.ordering()
    print(f"You have ordered:\n{user}")


if __name__ == "__main__":
    main()