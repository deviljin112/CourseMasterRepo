# Imports the test modules
import pytest
import unittest

# Imports the class for testing
from factory import BreadFactory


# Creates the Test Class which extends the unittest module
class TestFactory(unittest.TestCase):
    # Creates an instance of the BreadFactory class
    tested_class = BreadFactory()

    # Creates test case for each function in tested_class
    def test_dough(self):
        # Checks if with specified input in the function returns the expected result
        self.assertTrue(self.tested_class.make_dough(True, True))

    def test_naan(self):
        self.assertEqual(self.tested_class.bake_naan(True), "naan")

    def test_run(self):
        self.assertEqual(self.tested_class.run_factory(["water", "flour"]), "naan")
