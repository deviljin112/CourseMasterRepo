# Getters and Setters
# Used to hide the data
# Create a private variable

# Getter, fetches a hidden variable and returns it for printing
# Setter, edits the hidden variable for future uses


class Student:
    def __init__(self, name, company):
        # '__' makes a hidden variable unavailable for editing
        self.__name = name
        self.__company = company

    # Property makes the function act like a variable
    @property
    def studentName(self):
        return self.__name

    # Sets the value for the function
    @studentName.setter
    def studentName(self, new_name):
        self.__name = new_name


dev = Student("Dev", "Sparta")

# print(dev.__name) # Error this variable doesn't exist
print(dev.studentName)  # => Dev
dev.studentName = "Hubert"  # Property acts like a variable
print(dev.studentName)  # => Hubert
