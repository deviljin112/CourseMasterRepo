# Python-Bread-Factory-Task

## Requirements

You will need the following modules to use this project:

- `import pytest`
- `import unittest`

If you do not have `pytest` installed use `pip install pytest` in your terminal.

## Test Syntax

- `pytest` for basic testing utility
- `pytest -v` for more in-depth testing reporting

## First iteration

First we going to create the test code that we will run and expect it to fail all tests. This code will be used as a guidelines for what is required of our program, keep us focused on what needs to work, and how. As well as what the returned values should be of each function.

```python
# Creates the Test Class which extends the unittest module
class TestFactory(unittest.TestCase):
    # Creates an instance of the BreadFactory class
    tested_class = BreadFactory()

    # Creates test cases for each function
    def test_dough(self):
        # Checks if with specified input, the function returns the expected result
        self.assertTrue(self.tested_class.make_dough(True, True))

    def test_naan(self):
        self.assertEqual(self.tested_class.bake_naan(True), "naan")

    def test_run(self):
        self.assertEqual(self.tested_class.run_factory(["water", "flour"]), "naan")
```

### First Test Result

```bash
================================================= test session starts =================================================
platform win32 -- Python 3.9.0, pytest-6.1.2, py-1.9.0, pluggy-0.13.1 -- c:\python39\python.exe
cachedir: .pytest_cache
rootdir: .\Python-Bread-Factory-Task
collected 3 items

test_factory.py::TestFactory::test_dough FAILED                                                                  [ 33%]
test_factory.py::TestFactory::test_naan FAILED                                                                   [ 66%]
test_factory.py::TestFactory::test_run FAILED                                                                    [100%]

====================================================== FAILURES =======================================================
```

## Second Iteration

On our second iteration we create the code for passing the test and run the test again. We need to create our functions that we will be testing with arguments that will be passed from the test. Each function needs to return the Expected result that we have set in our tests.

```python
class BreadFactory:
    # Function for checking if user can make dough
    def make_dough(self, has_water, has_flour):
        if has_water and has_flour:
            # Returns True if user has BOTH water and flour
            return True
        else:
            return False

    # Function for checking if user can bake a naan bread
    def bake_naan(self, has_dough):
        if has_dough:
            # Returns string "naan" if user already made dough
            return "naan"
        return "failed"

    # Main function for running the whole factory
    # Input is a list of all ingredients available
    def run_factory(self, ingredients):
        # Sets local variables for future use
        has_water = False
        has_flour = False

        # If water and flour is in the ingredients list then set variables to true
        if "water" in ingredients and "flour" in ingredients:
            has_water = True
            has_flour = True

        # Check if user can make dough
        dough = self.make_dough(has_water, has_flour)
        # Check if user can make a naan bread
        naan = self.bake_naan(dough)
        # Return the result of previous function (either "naan" or "failed")
        return naan
```

### Second Test Result

```bash
================================================= test session starts =================================================
platform win32 -- Python 3.9.0, pytest-6.1.2, py-1.9.0, pluggy-0.13.1 -- c:\python39\python.exe
cachedir: .pytest_cache
rootdir: .\Python-Bread-Factory-Task
collected 3 items

test_factory.py::TestFactory::test_dough PASSED                                                                  [ 33%]
test_factory.py::TestFactory::test_naan PASSED                                                                   [ 66%]
test_factory.py::TestFactory::test_run PASSED                                                                    [100%]

================================================== 3 passed in 0.05s ==================================================
```

#### Step by Step Code Break-down

1. `run_factory()` function is the main function that will be ran by the user. This function takes a list which contains all the ingredients that the user has.
2. That list is assigned to the `ingredients` variable.
3. Next, we set our local variables (`has_water` and `has_flour`) that will be used in other functions to default value of `False`.
4. We then check with the `in` function whether "water" and "flour" is actuall in the ingredients list.
5. If they are, we set our local variables `has_water` and `has_flour` to `True`.
6. We then check if the user can make dough with the `make_dough()` function with takes our two previously mentioned boolean variables as arguments.
7. The function returns either a `True` or a `False` boolean depending on what the two booleans `has_water` and `has_water` were set to.
8. Both booleans need to be `True` for `make_dough()` to return `True`.
9. Next we take our return value from `make_dough()` and assign it to the `dough` variable which we pass to our next function, `bake_naan()`.
10. This function checks if the user has made dough, and if `True` returns the string `naan`.
11. If the user does not have dough; returns "failed".
12. The return value of this function is assigned to `naan` and returned from `run_factory()`.
