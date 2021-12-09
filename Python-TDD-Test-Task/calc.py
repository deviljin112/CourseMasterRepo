class Calculator:
    # Returns a value result from addition of val_1 and val_2
    def add(self, val_1, val_2):
        return val_1 + val_2

    def subtract(self, val_1, val_2):
        return val_1 - val_2

    def multiply(self, val_1, val_2):
        return val_1 * val_2

    def divide(self, val_1, val_2):
        return val_1 / val_2

    # Returns a boolean if val_1 is divisible by val_2
    def divisible(self, val_1, val_2):
        return val_1 % val_2 == 0

    # Returns a boolean if both values are positive (above 0)
    def positive(self, val_1, val_2):
        return (val_1 >= 0) and (val_2 >= 0)