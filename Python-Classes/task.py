# Creates a class called Cat
class Cat:
    # Creates a class variables accessible and modifiable by each instance
    name = "Paw"
    age = 8

    # Creates a class function that remains the same for each instance
    def meow(self):
        return "meow"


# Creates a new instance of the Cat class
paw = Cat()
# Print all class variables and function return
print(f"Paw: {paw.meow()}")
print(f"Paw: {paw.name}")
print(f"Paw: {paw.age}")

# Creates new instance of Cat class
sparkles = Cat()
# Changes the class variable only in this instance
sparkles.name = "Sparkles"
sparkles.age = 2
# Print all class variables and function return of this instance
print(f"Sparkles: {sparkles.meow()}")
print(f"Sparkles: {sparkles.name}")
print(f"Sparkles: {sparkles.age}")

# Same as sparkles with different data in class variables
milk = Cat()
milk.name = "Milk"
milk.age = 5
print(f"Milk: {milk.meow()}")
print(f"Milk: {milk.name}")
print(f"Milk: {milk.age}")