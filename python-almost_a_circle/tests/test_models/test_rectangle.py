#!/usr/bin/python3
"""Unit tests for the Rectangle class."""
import io
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


if __name__ == "__main__":
    unittest.main()
