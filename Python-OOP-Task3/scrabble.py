# Creates a Scrabble class
class Scrabble:
    # Initialises the class with a input of the word used for scoring
    def __init__(self, word):
        # Creates tables for each score
        self.value_1 = ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"]
        self.value_2 = ["D", "G"]
        self.value_3 = ["B", "C", "M", "P"]
        self.value_4 = ["F", "H", "V", "W", "Y"]
        self.value_5 = ["K"]
        self.value_8 = ["J", "X"]
        self.value_10 = ["Q", "Z"]
        # Assigns the input to a class variable
        self.word = word

    # Function for counting the score
    def count_score(self):
        # Breaks the word into single letters
        letters = [k for k in self.word]

        # Counts the score
        score = 0
        # Loops through each letter
        for i in letters:
            # Checks if the letter is in any class variable list
            if i in self.value_1:
                # If so add respective points
                score += 1
            elif i in self.value_2:
                score += 2
            elif i in self.value_3:
                score += 3
            elif i in self.value_4:
                score += 4
            elif i in self.value_5:
                score += 5
            elif i in self.value_8:
                score += 8
            elif i in self.value_10:
                score += 10

        # Returns the final score
        return score


def main():
    # Input for the word used to calculate the score
    word = input("Please provide a word for scoring\n=> ")

    # Intialisation of the class
    game = Scrabble(word.upper())
    # Final print of the score
    print(f"Word Scored: {game.count_score()} points")


if __name__ == "__main__":
    main()