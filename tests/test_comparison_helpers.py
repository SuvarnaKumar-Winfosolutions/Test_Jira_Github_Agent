import unittest
import io
import sys
from src.utils.comparison_helpers import compare_number_to_fifty

class TestCompareNumberToFifty(unittest.TestCase):
    def setUp(self):
        """Redirect stdout to capture print statements before each test."""
        self.held_output = io.StringIO()
        sys.stdout = self.held_output

    def tearDown(self):
        """Restore stdout to its original state after each test."""
        sys.stdout = sys.__stdout__ # Reset stdout

    def test_greater_than_50_integer(self):
        """Test with an integer strictly greater than 50."""
        number = 51
        compare_number_to_fifty(number)
        self.assertEqual(self.held_output.getvalue(), f"The number {number} is greater than 50.\n")

        self.held_output.seek(0) # Reset StringIO for next assertion
        self.held_output.truncate(0)

        number = 100
        compare_number_to_fifty(number)
        self.assertEqual(self.held_output.getvalue(), f"The number {number} is greater than 50.\n")

    def test_greater_than_50_float(self):
        """Test with a float strictly greater than 50."""
        number = 50.1
        compare_number_to_fifty(number)
        self.assertEqual(self.held_output.getvalue(), f"The number {number} is greater than 50.\n")

        self.held_output.seek(0)
        self.held_output.truncate(0)

        number = 100.5
        compare_number_to_fifty(number)
        self.assertEqual(self.held_output.getvalue(), f"The number {number} is greater than 50.\n")

    def test_equal_to_50(self):
        """Test when the number is exactly 50."""
        number = 50
        compare_number_to_fifty(number)
        self.assertEqual(self.held_output.getvalue(), f"The number {number} is not greater than 50.\n")

    def test_less_than_50_integer(self):
        """Test with an integer less than 50."""
        number = 49
        compare_number_to_fifty(number)
        self.assertEqual(self.held_output.getvalue(), f"The number {number} is not greater than 50.\n")

        self.held_output.seek(0)
        self.held_output.truncate(0)

        number = -10
        compare_number_to_fifty(number)
        self.assertEqual(self.held_output.getvalue(), f"The number {number} is not greater than 50.\n")

    def test_less_than_50_float(self):
        """Test with a float less than 50."""
        number = 49.9
        compare_number_to_fifty(number)
        self.assertEqual(self.held_output.getvalue(), f"The number {number} is not greater than 50.\n")

        self.held_output.seek(0)
        self.held_output.truncate(0)

        number = 0.0
        compare_number_to_fifty(number)
        self.assertEqual(self.held_output.getvalue(), f"The number {number} is not greater than 50.\n")

    def test_returns_none(self):
        """Test that the function returns None as specified."""
        # Call the function (output is captured by setUp, but not asserted here)
        result_greater = compare_number_to_fifty(51)
        self.assertIsNone(result_greater)

        self.held_output.seek(0)
        self.held_output.truncate(0)

        result_equal = compare_number_to_fifty(50)
        self.assertIsNone(result_equal)

        self.held_output.seek(0)
        self.held_output.truncate(0)

        result_less = compare_number_to_fifty(49)
        self.assertIsNone(result_less)
