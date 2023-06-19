#!/usr/bin/python3

"""
 Unit test for thr rectangle class
"""


import unittest
from models.rectangle import Rectangle
from io import StringIO
import sys


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

    def test_setters(self):
        """
            test all setters
        """

        r = Rectangle(5, 6)
        r.width = 8
        r.height = 9

        self.assertEqual(r.width, 8, "width should be 8")
        self.assertEqual(r.height, 9, "height should be 9 ")

        with self.assertRaises(ValueError):
            r.width = -2
        with self.assertRaises(ValueError):
            r.height = -3

        with self.assertRaises(TypeError):
            r.width = "a"
        with self.assertRaises(TypeError):
            r.height = "b"

    def test_rectangle_funcs(self):
        """
            tests all methods such as area
        """

        r1 = Rectangle(2, 3)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(8, 7, 0, 0, 12)

        self.assertEqual(r1.area(), 6, "area should be 6 (2 x 3)")
        self.assertEqual(r2.area(), 20, "area should be 20 (2 x 10)")
        self.assertEqual(r3.area(), 56, "area should be 56 (8 x 7)")

        stored_out = StringIO()
        sys.stdout = stored_out

        r1.display()

        sys.stdout = sys.__stdout__

        actual_output = stored_out.getvalue().strip()

        expected_out = "##\n##\n##"
        self.assertEqual(actual_output, expected_out)

    def Test_update(self):
        """
            tests the update function
        """

        r1 = Rectangle(10, 10, 10, 10)
        test_out = StringIO()
        sys.stdout = test_out
        print(r1)
        test_out_val = test_out.getvalue().strip()
        sys.stdout = sys.__stdout__
        self.assertEqual(test_out_val, "[Rectangle] (1) 10/10 - 10/10")

        r1.update(89)
        sys.stdout = test_out
        print(r1)
        test_out_val = test_out.getvalue().strip()
        sys.stdout = sys.__stdout__
        self.assertEqual(test_out_val, "[Rectangle] (89) 10/10 - 10/10")

        r1.update(x=1, height=2, y=3, width=4)
        sys.stdout = test_out
        print(r1)
        test_out_val = test_out.getvalue().strip()
        sys.stdout = sys.__stdout__
        self.assertEqual(test_out_val, "[Rectangle] (89) 1/3 - 2/4")

    def Test_co_ord_display(self):
        """
            test co-ordinate display
        """

        r1 = Rectangle(2, 3, 2, 2)
        sys.stdout = stored_out
        r1.display()

        sys.stdout = sys.__stdout__

        actual_output1 = stored_out.getvalue().strip()

        self.assertEqual(actual_output1, "\n\n  ##\n  ##\n  ##")

    def Test_str(self):
        """
            this tests the str function
        """
        r1 = Rectangle(4, 6, 2, 1, 12)
        test_out = StringIO()
        sys.stdout = test_out
        print(r1)
        test_out_val = test_out.getvalue().strip()
        sys.stdout = sys.__stdout__
        self.assertEqual(test_out_val, "[Rectangle] (12) 2/1 - 4/6")

        r2 = Rectangle(5, 5, 1)
        sys.stdout = test_out
        print(r2)
        test_out_val = test_out.getvalue().strip()
        sys.stdout = sys.__stdout__
        self.assertEqual(test_out_val, "[Rectangle] (1) 1/0 - 5/5")


if __name__ == "__main__":
    unittest.main()
