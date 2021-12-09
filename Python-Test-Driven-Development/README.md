# Test Driven Development

## Type of testing

- Unit Testing
- Development focused on test

### Modules used to test

- PyTest (`pip install pytest`)
- UnitTest (included with python)

## Why TDD

TDD helps to minimise the risk of a failure. It increases the quality of a product and reduces the chance of sending faulty/broken product to production.

### Implementation

- File for testing
- File for code
- Run the tests
- Alter the code if test fails
- Run tests again until they pass

![TDD](tdd.jpg)

### Commands

- `python -m pytest` => Runs the test
- `python -m pytest -v` => Breakdown of the test
- `python -m unittest discover -v` => Breakdown of the test

### Naming conventions

Example:

- `simple_calc` => Main file
- `test_simple_calc` => Tested file

#### PyTest flow

- PyTest looks for a `test_*.py` file name
- PyTest looks for `test_*` function name
- It executes those files / functions
- Prints the result of the tests
- `-v` flag for used for more in-depth breakdown of the test

## Example implementation

```python
class TestCalc(unittest.TestCase):
    calc = SimpleCalc()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 4), 6)
```

## Example Output

```bash
================================================= test session starts =================================================
platform win32 -- Python 3.9.0, pytest-6.1.2, py-1.9.0, pluggy-0.13.1
rootdir: .\Python-Test-Driven-Development
collected 4 items

test_simple_calc.py ....                                                                                         [100%]

================================================== 4 passed in 0.04s ==================================================
```

## TASK

- Create a new repo
- Name `tdd_test_task`
- Create a test file
- Create a code file
- Implement Pseudo Code
- Create README
- Document steps to replicate the task

### Code

- Create a test to check if the number is divisible by 0
  - If True Pass the test
  - If False Fail the test
- Create a test to check if given values are positive
