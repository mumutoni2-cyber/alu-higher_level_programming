#!/usr/bin/python3
"""Unit tests for the Square class."""
import io
import json
import os
import unittest
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """Tests for Square."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_inheritance(self):
        s = Square(1)
        self.assertIsInstance(s, Rectangle)
        self.assertIsInstance(s, Base)

    def test_init(self):
        s = Square(5)
        self.assertEqual((s.size, s.width, s.height, s.x, s.y, s.id),
                         (5, 5, 5, 0, 0, 1))
        s = Square(3, 1, 2, 7)
        self.assertEqual((s.size, s.x, s.y, s.id), (3, 1, 2, 7))

    def test_missing_arg(self):
        with self.assertRaises(TypeError):
            Square()

    def test_validation(self):
        with self.assertRaises(TypeError) as cm:
            Square("1")
        self.assertEqual(str(cm.exception), "width must be an integer")
        with self.assertRaises(ValueError) as cm:
            Square(0)
        self.assertEqual(str(cm.exception), "width must be > 0")
        with self.assertRaises(TypeError) as cm:
            Square(1, "a")
        self.assertEqual(str(cm.exception), "x must be an integer")
        with self.assertRaises(ValueError) as cm:
            Square(1, 0, -1)
        self.assertEqual(str(cm.exception), "y must be >= 0")

    def test_str(self):
        self.assertEqual(str(Square(5)), "[Square] (1) 0/0 - 5")
        self.assertEqual(str(Square(2, 2)), "[Square] (2) 2/0 - 2")
        self.assertEqual(str(Square(3, 1, 3)), "[Square] (3) 1/3 - 3")

    def test_area_display(self):
        s = Square(2, 2)
        self.assertEqual(s.area(), 4)
        with patch("sys.stdout", new=io.StringIO()) as out:
            s.display()
        self.assertEqual(out.getvalue(), "  ##\n  ##\n")

    def test_size_setter(self):
        s = Square(5)
        s.size = 10
        self.assertEqual((s.size, s.width, s.height), (10, 10, 10))
        self.assertEqual(str(s), "[Square] (1) 0/0 - 10")

    def test_size_setter_invalid(self):
        s = Square(5)
        with self.assertRaises(TypeError) as cm:
            s.size = "9"
        self.assertEqual(str(cm.exception), "width must be an integer")
        with self.assertRaises(ValueError) as cm:
            s.size = -1
        self.assertEqual(str(cm.exception), "width must be > 0")

    def test_update_args(self):
        s = Square(5)
        s.update(10)
        self.assertEqual(str(s), "[Square] (10) 0/0 - 5")
        s.update(1, 2)
        self.assertEqual(str(s), "[Square] (1) 0/0 - 2")
        s.update(1, 2, 3)
        self.assertEqual(str(s), "[Square] (1) 3/0 - 2")
        s.update(1, 2, 3, 4)
        self.assertEqual(str(s), "[Square] (1) 3/4 - 2")
        s.update(1, 2, 3, 4, 5, 6)
        self.assertEqual(str(s), "[Square] (1) 3/4 - 2")

    def test_update_kwargs(self):
        s = Square(5)
        s.update(x=12)
        self.assertEqual(str(s), "[Square] (1) 12/0 - 5")
        s.update(size=7, y=1)
        self.assertEqual(str(s), "[Square] (1) 12/1 - 7")
        s.update(size=7, id=89, y=1)
        self.assertEqual(str(s), "[Square] (89) 12/1 - 7")

    def test_update_args_skip_kwargs(self):
        s = Square(5)
        s.update(3, size=99)
        self.assertEqual((s.id, s.size), (3, 5))

    def test_update_unknown_kwarg(self):
        s = Square(5)
        s.update(foo=1)
        self.assertFalse(hasattr(s, "foo"))

    def test_update_invalid(self):
        s = Square(5)
        with self.assertRaises(TypeError):
            s.update(1, "a")

    def test_to_dictionary(self):
        s1 = Square(10, 2, 1)
        d = s1.to_dictionary()
        self.assertIs(type(d), dict)
        self.assertEqual(d, {"id": 1, "size": 10, "x": 2, "y": 1})
        s2 = Square(1, 1)
        s2.update(**d)
        self.assertEqual(str(s1), str(s2))
        self.assertIsNot(s1, s2)


class TestSquareSpec(unittest.TestCase):
    """Explicit spec-case tests for Square."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def tearDown(self):
        if os.path.exists("Square.json"):
            os.remove("Square.json")

    def test_init_one_arg(self):
        s = Square(1)
        self.assertEqual((s.size, s.x, s.y), (1, 0, 0))

    def test_init_two_args(self):
        s = Square(1, 2)
        self.assertEqual((s.x, s.y), (2, 0))

    def test_init_three_args(self):
        s = Square(1, 2, 3)
        self.assertEqual((s.x, s.y), (2, 3))

    def test_init_four_args(self):
        self.assertEqual(Square(1, 2, 3, 4).id, 4)

    def test_size_string(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("1")

    def test_x_string(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "2")

    def test_y_string(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, "3")

    def test_size_negative(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1)

    def test_x_negative(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(1, -2)

    def test_y_negative(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(1, 2, -3)

    def test_size_zero(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)

    def test_str_spec(self):
        self.assertEqual(str(Square(1, 2, 3, 4)), "[Square] (4) 2/3 - 1")

    def test_to_dictionary_spec(self):
        self.assertEqual(Square(1, 2, 3, 4).to_dictionary(),
                         {"id": 4, "size": 1, "x": 2, "y": 3})

    def test_update_no_args(self):
        s = Square(1, 2, 3, 4)
        s.update()
        self.assertEqual(str(s), "[Square] (4) 2/3 - 1")

    def test_update_args_each(self):
        s = Square(5, 5, 5, 1)
        s.update(89)
        self.assertEqual(s.id, 89)
        s.update(89, 1)
        self.assertEqual(s.size, 1)
        s.update(89, 1, 2)
        self.assertEqual(s.x, 2)
        s.update(89, 1, 2, 3)
        self.assertEqual(s.y, 3)

    def test_update_kwargs_each(self):
        s = Square(5, 5, 5, 1)
        s.update(**{'id': 89})
        self.assertEqual(s.id, 89)
        s.update(**{'id': 89, 'size': 1})
        self.assertEqual(s.size, 1)
        s.update(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(s.x, 2)
        s.update(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(s.y, 3)

    def test_create_each(self):
        self.assertEqual(Square.create(**{'id': 89}).id, 89)
        s = Square.create(**{'id': 89, 'size': 1})
        self.assertEqual(s.size, 1)
        s = Square.create(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(s.x, 2)
        s = Square.create(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(str(s), "[Square] (89) 2/3 - 1")

    def test_save_to_file_none(self):
        Square.save_to_file(None)
        with open("Square.json") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_empty(self):
        Square.save_to_file([])
        with open("Square.json") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_one(self):
        Square.save_to_file([Square(1, 0, 0, 7)])
        with open("Square.json") as f:
            self.assertEqual(json.loads(f.read()),
                             [{"id": 7, "size": 1, "x": 0, "y": 0}])

    def test_load_from_file_missing(self):
        self.assertEqual(Square.load_from_file(), [])

    def test_load_from_file_exists(self):
        Square.save_to_file([Square(1, 2, 3, 4)])
        out = Square.load_from_file()
        self.assertEqual(len(out), 1)
        self.assertEqual(str(out[0]), "[Square] (4) 2/3 - 1")


if __name__ == "__main__":
    unittest.main()
