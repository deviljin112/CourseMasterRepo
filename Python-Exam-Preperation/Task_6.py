class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def main():
    test = Person("Merry", 40)
    print(test.name)
    print(test.age)


if __name__ == "__main__":
    main()
