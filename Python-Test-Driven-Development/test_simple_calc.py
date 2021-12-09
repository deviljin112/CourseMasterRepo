import unittest
import pytest
from simple_calc import SimpleCalc


# unittest framework as parent class
class TestCalc(unittest.TestCase):
    # Creates instance of our class
    calc = SimpleCalc()

    # IMPORTANT
    # We must use the keyword "test" for interpeter to know we are testing
    def test_add(self):
        # Check if the result from the function matches the test
        self.assertEqual(self.calc.add(2, 4), 6)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(4, 2), 2)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 2), 4)

    def test_divide(self):
        self.assertEqual(self.calc.divide(4, 2), 2)
