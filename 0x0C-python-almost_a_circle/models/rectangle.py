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
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if height < 1:
            raise ValueError("height must be > 0")
        if width < 1:
            raise ValueError("width must be > 0")
        if x < 0:
            raise ValueError("x must >= 0")
        if y < 0:
            raise ValueError("y must >= 0")
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

        if not isinstance(value, int):
            raise TypeError("width must be integer")
        elif width < 1:
            raise ValueError("width must be > 0")
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

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif height < 1:
            raise ValueError("height must be > 0")
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

        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
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

        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value
