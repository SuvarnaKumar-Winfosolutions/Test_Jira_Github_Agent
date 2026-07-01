import unittest
from proj1.utils.number_helpers import classify_number_parity

class TestClassifyNumberParity(unittest.TestCase):

    def test_positive_even_number(self):
        self.assertEqual(classify_number_parity(4), "even")

    def test_zero_is_even(self):
        self.assertEqual(classify_number_parity(0), "even")

    def test_negative_even_number(self):
        self.assertEqual(classify_number_parity(-2), "even")

    def test_positive_odd_number(self):
        self.assertEqual(classify_number_parity(7), "odd")

    def test_negative_odd_number(self):
        self.assertEqual(classify_number_parity(-3), "odd")

    def test_non_integer_float_input_raises_type_error(self):
        with self.assertRaisesRegex(TypeError, "Input must be an integer, got float"):
            classify_number_parity(4.0)

    def test_non_integer_string_input_raises_type_error(self):
        with self.assertRaisesRegex(TypeError, "Input must be an integer, got str"):
            classify_number_parity("hello")

    def test_non_integer_none_input_raises_type_error(self):
        with self.assertRaisesRegex(TypeError, "Input must be an integer, got NoneType"):
            classify_number_parity(None)

    def test_non_integer_list_input_raises_type_error(self):
        with self.assertRaisesRegex(TypeError, "Input must be an integer, got list"):
            classify_number_parity([1, 2])
