class Dog:
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour
        self.animal_kind = "Husky"

    def bark(self):
        return "woof"


fido = Dog("Fido", "Black")

print(fido.animal_kind)
print(fido.name)
print(fido.colour)
print(fido.bark())