#!/usr/bin/python3
"""Unit tests for the Rectangle class."""
import io
import json
import os
import unittest
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Tests for Rectangle."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_inheritance(self):
        self.assertIsInstance(Rectangle(1, 2), Base)

    def test_ids(self):
        self.assertEqual(Rectangle(10, 2).id, 1)
        self.assertEqual(Rectangle(2, 10).id, 2)
        self.assertEqual(Rectangle(10, 2, 0, 0, 12).id, 12)

    def test_attributes(self):
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual((r.width, r.height, r.x, r.y, r.id),
                         (1, 2, 3, 4, 5))

    def test_defaults(self):
        r = Rectangle(1, 2)
        self.assertEqual((r.x, r.y), (0, 0))

    def test_missing_args(self):
        with self.assertRaises(TypeError):
            Rectangle()
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_type_errors(self):
        for bad in ("2", 2.5, None, {}, [], (1,), True):
            for name in ("width", "height", "x", "y"):
                kw = {"width": 1, "height": 1}
                if name in ("x", "y"):
                    kw[name] = bad
                else:
                    kw[name] = bad
                with self.assertRaises(TypeError) as cm:
                    Rectangle(**kw)
                self.assertEqual(str(cm.exception),
                                 "{} must be an integer".format(name))

    def test_type_error_setters(self):
        r = Rectangle(1, 1)
        for name in ("width", "height", "x", "y"):
            with self.assertRaises(TypeError) as cm:
                setattr(r, name, "a")
            self.assertEqual(str(cm.exception),
                             "{} must be an integer".format(name))

    def test_value_errors_width_height(self):
        for name in ("width", "height"):
            for bad in (0, -1):
                kw = {"width": 1, "height": 1}
                kw[name] = bad
                with self.assertRaises(ValueError) as cm:
                    Rectangle(**kw)
                self.assertEqual(str(cm.exception),
                                 "{} must be > 0".format(name))
                r = Rectangle(1, 1)
                with self.assertRaises(ValueError):
                    setattr(r, name, bad)

    def test_value_errors_x_y(self):
        with self.assertRaises(ValueError) as cm:
            Rectangle(1, 1, -1)
        self.assertEqual(str(cm.exception), "x must be >= 0")
        with self.assertRaises(ValueError) as cm:
            Rectangle(1, 1, 3, -1)
        self.assertEqual(str(cm.exception), "y must be >= 0")
        r = Rectangle(1, 1)
        r.x = 0
        r.y = 0

    def test_validation_order(self):
        with self.assertRaises(TypeError) as cm:
            Rectangle("a", 0)
        self.assertEqual(str(cm.exception), "width must be an integer")

    def test_setters_valid(self):
        r = Rectangle(1, 1)
        r.width, r.height, r.x, r.y = 5, 6, 7, 8
        self.assertEqual((r.width, r.height, r.x, r.y), (5, 6, 7, 8))

    def test_area(self):
        self.assertEqual(Rectangle(3, 2).area(), 6)
        self.assertEqual(Rectangle(2, 10).area(), 20)
        self.assertEqual(Rectangle(8, 7, 0, 0, 12).area(), 56)

    def _display(self, r):
        with patch("sys.stdout", new=io.StringIO()) as out:
            r.display()
        return out.getvalue()

    def test_display_basic(self):
        self.assertEqual(self._display(Rectangle(2, 2)), "##\n##\n")
        self.assertEqual(self._display(Rectangle(4, 6)),
                         "####\n" * 6)

    def test_display_xy(self):
        self.assertEqual(self._display(Rectangle(2, 3, 2, 2)),
                         "\n\n  ##\n  ##\n  ##\n")
        self.assertEqual(self._display(Rectangle(3, 2, 1, 0)),
                         " ###\n ###\n")

    def test_str(self):
        self.assertEqual(str(Rectangle(4, 6, 2, 1, 12)),
                         "[Rectangle] (12) 2/1 - 4/6")
        self.assertEqual(str(Rectangle(5, 5, 1)),
                         "[Rectangle] (1) 1/0 - 5/5")

    def test_update_args(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(89)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 10/10")
        r.update(89, 2)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 2/10")
        r.update(89, 2, 3)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 2/3")
        r.update(89, 2, 3, 4)
        self.assertEqual(str(r), "[Rectangle] (89) 4/10 - 2/3")
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_args_extra_ignored(self):
        r = Rectangle(1, 1)
        r.update(1, 2, 3, 4, 5, 6, 7)
        self.assertEqual(r.to_dictionary(),
                         {"id": 1, "width": 2, "height": 3, "x": 4, "y": 5})

    def test_update_kwargs(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(height=1)
        self.assertEqual(str(r), "[Rectangle] (1) 10/10 - 10/1")
        r.update(width=1, x=2)
        self.assertEqual(str(r), "[Rectangle] (1) 2/10 - 1/1")
        r.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(r), "[Rectangle] (89) 3/1 - 2/1")
        r.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(r), "[Rectangle] (89) 1/3 - 4/2")

    def test_update_args_skip_kwargs(self):
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(5, width=99)
        self.assertEqual(r.id, 5)
        self.assertEqual(r.width, 10)

    def test_update_unknown_kwarg(self):
        r = Rectangle(1, 1)
        r.update(foo=1)
        self.assertFalse(hasattr(r, "foo"))

    def test_update_no_args(self):
        r = Rectangle(1, 2, 3, 4, 5)
        r.update()
        self.assertEqual(str(r), "[Rectangle] (5) 3/4 - 1/2")

    def test_update_invalid(self):
        r = Rectangle(1, 1)
        with self.assertRaises(TypeError):
            r.update(1, "a")
        with self.assertRaises(ValueError):
            r.update(width=-1)

    def test_to_dictionary(self):
        r1 = Rectangle(10, 2, 1, 9)
        d = r1.to_dictionary()
        self.assertIs(type(d), dict)
        self.assertEqual(d, {"id": 1, "width": 10, "height": 2,
                             "x": 1, "y": 9})
        r2 = Rectangle(1, 1)
        r2.update(**d)
        self.assertEqual(str(r1), str(r2))
        self.assertIsNot(r1, r2)


class TestRectangleSpec(unittest.TestCase):
    """Explicit spec-case tests for Rectangle."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def tearDown(self):
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")

    def test_init_two_args(self):
        r = Rectangle(1, 2)
        self.assertEqual((r.width, r.height, r.x, r.y), (1, 2, 0, 0))

    def test_init_three_args(self):
        r = Rectangle(1, 2, 3)
        self.assertEqual((r.x, r.y), (3, 0))

    def test_init_four_args(self):
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual((r.x, r.y), (3, 4))

    def test_init_five_args(self):
        self.assertEqual(Rectangle(1, 2, 3, 4, 5).id, 5)

    def test_width_string(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("1", 2)

    def test_height_string(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "2")

    def test_x_string(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, "3")

    def test_y_string(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, "4")

    def test_width_negative(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-1, 2)

    def test_height_negative(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, -2)

    def test_width_zero(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)

    def test_height_zero(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, 0)

    def test_x_negative(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(1, 2, -3)

    def test_y_negative(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(1, 2, 3, -4)

    def test_area_spec(self):
        self.assertEqual(Rectangle(3, 4).area(), 12)

    def test_str_spec(self):
        self.assertEqual(str(Rectangle(1, 2, 3, 4, 5)),
                         "[Rectangle] (5) 3/4 - 1/2")

    def test_display_without_x_and_y(self):
        with patch("sys.stdout", new=io.StringIO()) as out:
            Rectangle(2, 3).display()
        self.assertEqual(out.getvalue(), "##\n##\n##\n")

    def test_display_without_y(self):
        with patch("sys.stdout", new=io.StringIO()) as out:
            Rectangle(2, 3, 1).display()
        self.assertEqual(out.getvalue(), " ##\n ##\n ##\n")

    def test_display_with_x_and_y(self):
        with patch("sys.stdout", new=io.StringIO()) as out:
            Rectangle(2, 2, 1, 1).display()
        self.assertEqual(out.getvalue(), "\n ##\n ##\n")

    def test_to_dictionary_spec(self):
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.to_dictionary(),
                         {"id": 5, "width": 1, "height": 2,
                          "x": 3, "y": 4})

    def test_update_no_args(self):
        r = Rectangle(1, 2, 3, 4, 5)
        r.update()
        self.assertEqual(r.to_dictionary(),
                         {"id": 5, "width": 1, "height": 2,
                          "x": 3, "y": 4})

    def test_update_args_each(self):
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(89)
        self.assertEqual(r.id, 89)
        r.update(89, 1)
        self.assertEqual(r.width, 1)
        r.update(89, 1, 2)
        self.assertEqual(r.height, 2)
        r.update(89, 1, 2, 3)
        self.assertEqual(r.x, 3)
        r.update(89, 1, 2, 3, 4)
        self.assertEqual(r.y, 4)

    def test_update_kwargs_each(self):
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(**{'id': 89})
        self.assertEqual(r.id, 89)
        r.update(**{'id': 89, 'width': 1})
        self.assertEqual(r.width, 1)
        r.update(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(r.height, 2)
        r.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual(r.x, 3)
        r.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(r.y, 4)

    def test_create_id(self):
        r = Rectangle.create(**{'id': 89})
        self.assertEqual(r.id, 89)

    def test_create_width(self):
        r = Rectangle.create(**{'id': 89, 'width': 1})
        self.assertEqual((r.id, r.width), (89, 1))

    def test_create_height(self):
        r = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual((r.width, r.height), (1, 2))

    def test_create_x(self):
        r = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2,
                                'x': 3})
        self.assertEqual(r.x, 3)

    def test_create_y(self):
        r = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2,
                                'x': 3, 'y': 4})
        self.assertEqual(str(r), "[Rectangle] (89) 3/4 - 1/2")

    def test_save_to_file_none(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_empty(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_one(self):
        Rectangle.save_to_file([Rectangle(1, 2, 0, 0, 7)])
        with open("Rectangle.json") as f:
            self.assertEqual(
                json.loads(f.read()),
                [{"id": 7, "width": 1, "height": 2, "x": 0, "y": 0}])

    def test_load_from_file_missing(self):
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_load_from_file_exists(self):
        Rectangle.save_to_file([Rectangle(1, 2, 3, 4, 5)])
        out = Rectangle.load_from_file()
        self.assertEqual(len(out), 1)
        self.assertEqual(str(out[0]), "[Rectangle] (5) 3/4 - 1/2")


if __name__ == "__main__":
    unittest.main()
