###########
# Classes #
###########

# Create class
# Syntax: class Name:


class Dog:
    def __init__(self):
        pass

    # Define a class variable
    animal_kind = "Husky"

    # Create a function in the class
    def bark(self):
        return "woof"


foo = Dog()
print(foo.bark())
print(foo.animal_kind)

bar = Dog()
print(bar.bark())
print(bar.animal_kind)

foo.animal_kind = "York-shire"
print(foo.animal_kind)
print(bar.animal_kind)

# Inherit class
# Syntax: class Name(Parent_name):
