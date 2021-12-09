# Creates a class called FizzBuzz
class FizzBuzz:
    # Initialises the class with 2 input variables
    def __init__(self, div_1, div_2):
        # Creates a list with 1 through 100
        self.numbers = [k for k in range(101) if k != 0]
        # Assigns 2 inputs to class variables
        self.fizz = div_1
        self.buzz = div_2

    # Creates a class function
    def check_numbers(self):
        # Loops through all values in the list
        for i in range(len(self.numbers)):
            # If the number is divisible by fizz variable or buzz variable
            if self.numbers[i] % self.fizz and self.numbers[i] % self.buzz:
                # Make that value "FizzBuzz"
                self.numbers[i] = "FizzBuzz"
            # If the number is only divisble by fizz variable
            elif self.numbers[i] % self.fizz:
                # Then make that value "Fizz"
                self.numbers[i] = "Fizz"
            elif self.numbers[i] % self.buzz:
                self.numbers[i] = "Buzz"

        # This function returns a string for clear formating
        return " ".join(str(x) for x in self.numbers)

    # This function is used when we print the class by itself
    def __str__(self):
        # The return value is the self.numbers list
        return " ".join(str(x) for x in self.numbers)

# The main function
def main():
    # Takes two inputs which are integers for division
    fizz = input("What should be the divider number for 'Fizz'?\n=> ")
    buzz = input("What should be the divider number for 'Buzz'?\n=> ")

    # Checks that the input is a number
    if fizz.isdigit() and buzz.isdigit():
        # Casts the strings into integers
        fizz, buzz = int(fizz), int(buzz)
        # Initialises the class with the two numbers
        game = FizzBuzz(fizz, buzz)

        # Prints the numbers from 1 - 100
        print(game)
        # Prints the numbers with "Fizz", "Buzz" and "FizzBuzz" included
        print(game.check_numbers())
    else:
        print("You need to use integer numbers!")


# Only run when this is the main file
if __name__ == "__main__":
    main()
