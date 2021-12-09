# Python-TDD-Test-Task

## Requirements

You will need to import the following modules into your project:

- `import unittest`
- `import pytest`

## Initialising the Test Code

First we need to create a class that will act as the testing environment. To do that we need to inherit from the `unittest.TestCase`. Then we need to make a class variable that will create an instance of the class we will be testing.

```python
class TestCalc(unittest.TestCase):
    tested_class = Calculator()
```

### Creating test cases (methods)

Test methods are similar to regular methods/functions. However, their naming should follow the standard conventions of `test_function_name`. This tells the `unittest` and `pytest` module that this will be a test case method. We then use the `assert` function which will be used to check whether the return value from the called function is equal to expected results.
</br>
In the following example we can see that we checking for equality with `assetEqual` this takes an argument of the function we trying to check and the expected result. In our case we wnat to test the `add()` functino from `Calculator` class which is assigned to the `tested_class` variable. We can call that function and pass arguments to it, and the `assertEqual` will check if the returned value matches with our expected value.

```python
def test_add(self):
    self.assertEqual(self.tested_class.add(2, 4), 6)
```

Another use of assert can be checking for boolean values. To do this we will be using the `assertTrue` function. Unlike `assertEqual`, this function only takes one argument, which is the function we are testing and checks if the return value is `True`. There is also an alternative of `assertFalse` to check the opposite result.

```python
def test_divisible(self):
    self.assertTrue(self.tested_class.divisible(4, 2))
```

## What we testing

The functions in the `Calculator` class need to have a return value for the tests to complete. Depending on the assert function you use you will need to return different values.

Example for `assertEqual`

```python
def add(self, val_1, val_2):
    return val_1 + val_2
```

Example for `assertTrue`

```python
def divisible(self, val_1, val_2):
    return val_1 % val_2 == 0
```

## How we are testing

In order to test our code, we need to open our terminal with our project focused. Then we need to run the `python -m pytest` command and await the results. If there was an error it would mean that there is an issue in our code. We can also add the `-v` flag at the end of the command to see a more in-depth breakdown of the testing process. Each function that worked or didnt, and percentage progress of the testing process.
</br>
Example output:

```bash
================================================= test session starts =================================================
platform win32 -- Python 3.9.0, pytest-6.1.2, py-1.9.0, pluggy-0.13.1
rootdir: .\Python-Test-Driven-Development
collected 4 items

test_simple_calc.py ....                                                                                         [100%]

================================================== 4 passed in 0.04s ==================================================
```
