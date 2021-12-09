# OOP

## Step 1

- Create an Animal class as a Parent
- Using `class ClassName`
- We then initialise the class with `def __init__()`
- We can also specify what arguments the initialisation takes in brackets
- If we have an input argument we then put it as `self.argument = argument`

```python
class Animal:
    def __init__(self, alive):
        self.alive = alive
```

## Step 2

- Create reptile class as a child class
- Inherit from Animal parent
- Abstract
- To inherit from parent we need to import the class
  - Using `from file_name import ClassName`
- We also need to initialise the class same way as parent
- We can specify new/more variables inside of intialisation
- We then need to import the variables from parent
  - Using `super().__init__()`
  - If parent takes in an argument we need to specify them in our `__init__` if they dynamic, or hard code them in brackets
  - `super().__init__(argument)`

```python
from animal import Animal

class Reptile(Animal):
    def __init__(self, cold_blooded, tetrapod, amniotic_eggs):
        super().__init__(True)
        self.cold_blooded = cold_blooded
```

## Step 3

- Create snake class as child of reptile
- This step is the same as Step 2

```python
from reptile import Reptile

class Snake(Reptile):
    def __init__(self, venom):
        super().__init__(True, False, True)
```

## Step 4

- Create python class as child of snake
- This step is the same as Step 2

```python
from snake import Snake

class Python(Snake):
    def __init__(self):
        super().__init__(False)
```

## Name and Main

- `__name__` and `__main__` are used to check whether the code is the main file being ran or if it is bein imported
- By creating 2 files that use `__name__` and `__main__` it will show the difference
- File being imported will have a different name
- File that is the main file used, will have its name set to `__main__`

## Getters and Setters

- We can make private variables in the `__init__`.
- To do that we put `__` in front of the variable's name.
- We can then create a `@property` which is a function that has variable-like behaviours.
- A property doesnt need to be called with `()` instead the function has to return something, most often the hidden variable.
- To edit the hidden variable we then use `@function_name.setter` this way we can alter / edit the hidden variable and adjust the input data so it matches our formatting.
- The common use of Getter and Setter is for data manipulation to ensure that the format is intact and remains the same.
- Another common use is to hide important variables so that the user cannot change/break the software by providing unexpected data.
