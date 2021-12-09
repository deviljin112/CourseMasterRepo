# Import the test modules
import unittest
import pytest

# Import the class we will be testing
from calc import Calculator

# Test class, extends unit testing
class TestCalc(unittest.TestCase):
    # Creates an instance of Calculator class
    tested_class = Calculator()

    # Creates a method for testing
    # Prefixed with `test_`
    def test_add(self):
        # Checks if the return value is equal to specified value
        self.assertEqual(self.tested_class.add(2, 4), 6)

    def test_subtract(self):
        self.assertEqual(self.tested_class.subtract(4, 2), 2)

    def test_multiply(self):
        self.assertEqual(self.tested_class.multiply(2, 2), 4)

    def test_divide(self):
        self.assertEqual(self.tested_class.divide(4, 2), 2)

    def test_divisible(self):
        # Checks if the return value is True
        self.assertTrue(self.tested_class.divisible(4, 2))

    def test_positive(self):
        self.assertTrue(self.tested_class.positive(9, 11))