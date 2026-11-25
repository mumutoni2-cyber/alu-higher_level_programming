#!/usr/bin/python3
"""Unit tests for the Base class."""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Tests for Base."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def tearDown(self):
        for name in ("Base.json", "Rectangle.json", "Square.json"):
            if os.path.exists(name):
                os.remove(name)

    def test_auto_ids(self):
        self.assertEqual(Base().id, 1)
        self.assertEqual(Base().id, 2)
        self.assertEqual(Base().id, 3)

    def test_explicit_id(self):
        self.assertEqual(Base(12).id, 12)
        self.assertEqual(Base().id, 1)

    def test_id_none_and_other_values(self):
        self.assertEqual(Base(None).id, 1)
        self.assertEqual(Base(0).id, 0)
        self.assertEqual(Base(-4).id, -4)

    def test_to_json_string(self):
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        s = Base.to_json_string([{"id": 1}])
        self.assertIsInstance(s, str)
        self.assertEqual(s, '[{"id": 1}]')

    def test_from_json_string(self):
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])
        self.assertEqual(Base.from_json_string('[{"id": 1}]'), [{"id": 1}])

    def test_json_roundtrip(self):
        data = [{"id": 89, "width": 10}, {"id": 7, "width": 1}]
        out = Base.from_json_string(Base.to_json_string(data))
        self.assertEqual(out, data)

    def test_save_to_file_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 0, 0, 2)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json") as f:
            data = Base.from_json_string(f.read())
        self.assertEqual(data, [r1.to_dictionary(), r2.to_dictionary()])

    def test_save_to_file_square(self):
        s = Square(3, 1, 2, 5)
        Square.save_to_file([s])
        with open("Square.json") as f:
            self.assertEqual(Base.from_json_string(f.read()),
                             [s.to_dictionary()])

    def test_save_to_file_none_and_empty(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json") as f:
            self.assertEqual(f.read(), "[]")
        Square.save_to_file([])
        with open("Square.json") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_overwrites(self):
        Rectangle.save_to_file([Rectangle(1, 1)])
        Rectangle.save_to_file([])
        with open("Rectangle.json") as f:
            self.assertEqual(f.read(), "[]")

    def test_create_rectangle(self):
        r1 = Rectangle(3, 5, 1, 0, 9)
        r2 = Rectangle.create(**r1.to_dictionary())
        self.assertIsNot(r1, r2)
        self.assertEqual(str(r1), str(r2))
        self.assertIsInstance(r2, Rectangle)

    def test_create_square(self):
        s1 = Square(3, 1, 2, 9)
        s2 = Square.create(**s1.to_dictionary())
        self.assertIsNot(s1, s2)
        self.assertEqual(str(s1), str(s2))
        self.assertIsInstance(s2, Square)

    def test_create_base(self):
        class Dummy(Base):
            def update(self, *args, **kwargs):
                self.id = kwargs.get("id", self.id)
        self.assertEqual(Dummy.create(id=5).id, 5)

    def test_load_from_file_missing(self):
        self.assertEqual(Rectangle.load_from_file(), [])
        self.assertEqual(Square.load_from_file(), [])

    def test_load_from_file_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        out = Rectangle.load_from_file()
        self.assertEqual([str(r) for r in out], [str(r1), str(r2)])
        self.assertIsNot(out[0], r1)

    def test_load_from_file_square(self):
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        Square.save_to_file([s1, s2])
        out = Square.load_from_file()
        self.assertEqual([str(s) for s in out], [str(s1), str(s2)])
        self.assertTrue(all(isinstance(s, Square) for s in out))


if __name__ == "__main__":
    unittest.main()
