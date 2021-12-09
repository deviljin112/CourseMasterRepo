# Create a class
class Animal:
    # Initialise the class with variables and take in an input at initialisation
    def __init__(self, alive):
        self.alive = alive  # Creates a variable within the class
        self.spine = True
        self.eyes = True
        self.lungs = True

    # Creates a class function
    def breathe(self):
        # Returns a value when called upon
        return "Keep breathing!"

    def eat(self):
        return "Nom Nom"

    def procreate(self):
        return "Baby making in the process"

    def move(self):
        return "Stepped forward"
