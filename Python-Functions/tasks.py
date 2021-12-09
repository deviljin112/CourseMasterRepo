# Create a function that takes in two arguments as ints
# and adds them together
def addition(values):
    # Sets answer to 0
    answer = 0
    # Loops through all provided values
    for i in values:
        # Adds each value to answer
        answer += i
    # Returns the final answer so its available for printing etc.
    return answer


# Create a function that takes in two arguments as ints
# and subtracts them from each other
def subtraction(values):
    # Sets the first value as the answer
    answer = values[0]
    # Loops through each index of 'values'
    for i in range(len(values)):
        # If the index is not the first index do the action
        if i != 0:
            # Subtract value in specified index from the answer
            answer -= values[i]
    # Returns the final answer so its available for printing etc.
    return answer


## Task 1 ##
# Create a function for multiplication
def multiply(values):
    answer = values[0]
    for i in range(len(values)):
        if i != 0:
            answer *= values[i]
    return answer


## Task 2 ##
# Create a function for division
def divide(values):
    answer = values[0]
    for i in range(len(values)):
        if i != 0:
            answer /= values[i]
    return answer


## Task 3 ##
# Create a function for modulus
def modulo(values):
    answer = values[0]
    for i in range(len(values)):
        if i != 0:
            answer %= values[i]
    return answer


## Task 4 ##
# Create a function to take a number to the power of another
def power(values):
    answer = values[0]
    for i in range(len(values)):
        if i != 0:
            answer = answer ** values[i]
    return answer


# Function for printing the answer removes repeated Print Statements
def printer(answer):
    print(f"The answer is: {answer}")


# Main function is ran after all functions are stored in RAM
def main():
    # Creates all the options in a list for dynamic functionality
    options = ["add", "subtract", "multiply", "divide", "modulus", "power"]

    # Takes in an input from the user
    choice = input(
        f"""
What would you like to do?
Options: {" ".join(options).title()}
=> """
    )
    # Join() combines the list into a readable string and capitalises each word

    # Checks that the input is an available option
    if choice.lower() in options:
        # Asks for all the values that the user wants to modify
        values = input("What are your values?\nFormat: NUM NUM NUM ...\n=> ").split(" ")
        # Checks if the user gave more than 1 value
        if len(values) > 1:
            # Sets a boolean to keep track of the results in the next for loop
            are_digits = True

            # For loop to check if numbers are integers
            for i in range(len(values)):
                if values[i].isdigit():
                    # Changes string into a digit
                    values[i] = int(values[i])
                else:
                    return False

            # If they are digits check what the user wanted to do
            if are_digits:
                if choice.lower() == "add":
                    # Print the results of the operation
                    printer(addition(values))
                elif choice.lower() == "subtract":
                    printer(subtraction(values))
                elif choice.lower() == "multiply":
                    printer(multiply(values))
                elif choice.lower() == "divide":
                    printer(divide(values))
                elif choice.lower() == "modulus":
                    printer(modulo(values))
                elif choice.lower() == "power":
                    printer(power(values))
            # If they not digits print a prompt
            else:
                print("You need to input integer numbers!")
        # If theres only 1 value print a prompt
        else:
            print("You need to provide more than one value!")
    # If the choice is not in the list print a prompt
    else:
        print("That choice is not on the list!")


# Double under, so that all code is cached before execution
if __name__ == "__main__":
    main()