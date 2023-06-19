#!/usr/bin/python3

"""
 Unit test for thr rectangle class
"""


import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
        Test class for the rectangle class

        Args:
            Inherits the unittest.TestCase
    """
    def test_rect_ctreation(self):
        """
            this method test and ensures the code creates valid Id's
        """

        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1, "Id should be equal to 1")

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2, "Id should be equal to 2")

        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12, "Id should be equal to 12")

    def test_rect_invalid(self):
        """
            Test for invalid inputs and ensures the correct Error is raised
        """

        with self.assertRaises(TypeError):
            Rectangle('a', 3)
        with self.assertRaises(TypeError):
            Rectangle(3, 'a')
        with self.assertRaises(TypeError):
            Rectangle(1, 2, '3')
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, '4')
        with self.assertRaises(ValueError):
            Rectangle(-1, 1)
        with self.assertRaises(ValueError):
            Rectangle(1, -1)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)

if __name__ == "__main__":
    unittest.main()
