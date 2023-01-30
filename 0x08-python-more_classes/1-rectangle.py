#!/usr/bin/python3
"""Rectangle module"""


class Rectangle:
    """Defining a class Rectangle
    with optional width and length"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

        @property
        """Getter method for width"""
        def width(self):
            return self.__width

        @width.setter
        """Setter function for width"""
        def width(self, value):
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            elif value < 0:
                raise ValueError("width must be >= 0")
            self.__width = value

        @property
        """Getter method for height"""
        def height(self):
            return self.__height

        @height.setter
        """Setter method for height"""
        def height(self, value):
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            elif value < 0:
                raise ValueError("height must be >= 0")
            self.__height = value
