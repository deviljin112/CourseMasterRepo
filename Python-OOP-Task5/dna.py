class Dna:
    # Takes in a word
    def __init__(self, word):
        # Assigns that word to a variable
        self.word = word
        # Splits the word into a list of letters
        self.letters = [i for i in self.word]
        # Variable calls the function that returns a string
        self.unique = self.create_unique(self.letters)

    # Function for getting unique letters
    def create_unique(self, letters):
        # Creates an empty dictionary
        unique_dict = {}
        # Loops through all the letters
        for i in letters:
            # Adds the letter to the dictionary
            # Because dictionary can only have one unique key it will override it self and only return single letters as keys
            unique_dict[i] = 0

        # Returns the dictionary
        return unique_dict

    @property
    def count_unique(self):
        # Temporary dictionary holder
        unique_table = self.unique
        # Loops through all letters
        for i in self.letters:
            # Adds 1 to each letter count
            unique_table[i] += 1

        # Return a string of combined letter counts
        return " ".join(str(x) for x in unique_table.values())


def main():
    wordset = input("Please input your word for counting\n=> ")

    game = Dna(wordset)
    print(game.count_unique)


if __name__ == "__main__":
    main()