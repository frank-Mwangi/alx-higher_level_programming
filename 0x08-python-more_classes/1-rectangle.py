#!/usr/bin/python3
"""Rectangle module"""


class Rectangle:
    """Defining a class Rectangle
    with optional width and length"""

    def __init__(self, width=0, height=0):
        """Initializing an instance of the class Rectangle"""
        self.__width = width
        self.__height = height

        @property
        def width(self):
            """Getter method for width"""
            return self.__width

        @width.setter
        def width(self, value):
            """Setter method for private attribute width"""
            if type(value) is not int:
                raise TypeError("width must be an integer")
            elif value < 0:
                raise ValueError("width must be >= 0")
            self.__width = value

        @property
        def height(self):
            """Getting the private attribute height"""
            return self.__height

        @height.setter
        def height(self, value):
            """Setting the private attribute height"""
            if type(value) is not int:
                raise TypeError("height must be an integer")
            elif value < 0:
                raise ValueError("height must be >= 0")
            self.__height = value
