# Classes

## Object Oriented Programming

### Four Pillars of OOP

- Inheritance
  - Eliminates redundant code
- Encapsulation
  - Reduce complexity and increase reusability
- Abstraction
  - Reduce complexity and isolate impact of change
- Polymorphism
  - Poly (many) morphism (form) Refactor code or case statements
  - It allows us to change behaviours and/or attributes/variables

## Class

Class is the main factor that is used to implement any of the pillars.

### Creating a class

To create a class we need to use the `class` syntax followed by the name. We can then define class variables that will be accessible and editable by all instances of that class. We can also create functions, those functions will be available to all instances and cannot be altered.

```python
class ClassName:
    class_variable = "some_data"

    def function_name(self):
        return "some_other_data"
```

## Task

Available: [here](task.py)

- Create a cat class
- One function that returns "Meow"
- Create 2 class level variable
- Create 3 objects
- Display all information for each object
- Change the class variables' values in each object
- Display new data
- Sudo code each block
