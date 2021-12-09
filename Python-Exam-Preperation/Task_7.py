from Task_6 import Person


class Student(Person):
    def __init__(self, name, age, student_id, course):
        super().__init__(name, age)
        self.student_id = student_id
        self.course = course


def main():
    test = Student("Marry", 40, 1234, "DevOps")
    print(test.name)
    print(test.age)
    print(test.student_id)
    print(test.course)


if __name__ == "__main__":
    main()
