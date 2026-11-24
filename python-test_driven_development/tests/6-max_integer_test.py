#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer"""

    def test_ordered_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_max_in_middle(self):
        self.assertEqual(max_integer([1, 5, 2]), 5)

    def test_max_at_end(self):
        self.assertEqual(max_integer([3, 1, 9]), 9)

    def test_one_element(self):
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_no_argument(self):
        self.assertIsNone(max_integer())

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-5, -2, -9]), -2)

    def test_mixed_signs(self):
        self.assertEqual(max_integer([-1, 0, 1]), 1)

    def test_duplicates(self):
        self.assertEqual(max_integer([2, 8, 8, 1]), 8)

    def test_all_equal(self):
        self.assertEqual(max_integer([3, 3, 3]), 3)

    def test_floats(self):
        self.assertEqual(max_integer([1.5, 2.5, 0.5]), 2.5)

    def test_int_and_float(self):
        self.assertEqual(max_integer([1, 2.5, 2]), 2.5)

    def test_large_numbers(self):
        self.assertEqual(max_integer([10 ** 20, 5, 10 ** 19]), 10 ** 20)

    def test_tuple(self):
        self.assertEqual(max_integer((1, 4, 2)), 4)

    def test_string(self):
        self.assertEqual(max_integer("abc"), "c")

    def test_list_of_strings(self):
        self.assertEqual(max_integer(["a", "c", "b"]), "c")

    def test_list_not_modified(self):
        data = [3, 1, 2]
        max_integer(data)
        self.assertEqual(data, [3, 1, 2])

    def test_none_raises_type_error(self):
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_int_raises_type_error(self):
        with self.assertRaises(TypeError):
            max_integer(5)

    def test_mixed_types_raise_type_error(self):
        with self.assertRaises(TypeError):
            max_integer([1, "a", 3])


if __name__ == '__main__':
    unittest.main()
