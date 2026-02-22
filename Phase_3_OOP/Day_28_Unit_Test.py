import sys
import os
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from Phase_2_Files_Data.Day_19_Safe_Calc import calculate

class TestCalculator(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(calculate(10, 5, "+"), 15)
        self.assertEqual(calculate(-1, 1, "+"), 0)

    def test_division(self):
        self.assertEqual(calculate(10, 2, "/"), 5)
        
        with self.assertRaises(ZeroDivisionError):
            calculate(10, 0, "/")

    def test_invalid_operator(self):
        with self.assertRaises(ValueError):
            calculate(10, 5, "%")

if __name__ == "__main__":
    unittest.main()