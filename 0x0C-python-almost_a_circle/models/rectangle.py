#!/usr/bin/python3
"""
    the modules has a Rectangle class
"""


from models.base import Base


class Rectangle(Base):
    """
        The rectangle class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
            class initialisation

            Args:
                width (int, float): width
                height (int, float): height
                x (int, float): x
                y (int, float): y
                id (int): id

        """

        super().__init__(id)
        if not isinstance(width, (int, float)):
            raise TypeError("<width> should be an int ot float type")
        if not isinstance(height, (int, float)):
            raise TypeError("<height> should be an int ot float type")
        if not isinstance(x, (int, float)):
            raise TypeError("<x> should be an int ot float type")
        if not isinstance(y, (int, float)):
            raise TypeError("<y> should be an int ot float type")
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """
            this gets the value of the width
        """

        return self.__width

    @width.setter
    def width(self, value):
        """
            this sets width to value
        """

        if not isinstance(value, (int, float)):
            raise TypeError("<value should be int or float>")
        else:
            self.__width = value

    @property
    def height(self):
        """
            this gets the value of the height
        """

        return self.__height

    @height.setter
    def height(self, value):
        """
            this sets height to value
        """

        if not isinstance(value, (int, float)):
            raise TypeError("<value should be int or float>")
        else:
            self.__height = value

    @property
    def x(self):
        """
            this gets the value of the x
        """

        return self.__x

    @x.setter
    def x(self, value):
        """
            this sets x to value
        """

        if not isinstance(value, (int, float)):
            raise TypeError("<value should be int or float>")
        else:
            self.__x = value

    @property
    def y(self):
        """
            this gets the value of the x
        """

        return self.__y

    @y.setter
    def y(self, value):
        """
            this sets y to value
        """

        if not isinstance(value, (int, float)):
            raise TypeError("<value should be int or float>")
        else:
            self.__y = value
