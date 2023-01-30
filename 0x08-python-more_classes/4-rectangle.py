#!/usr/bin/python3
"""
Rectangle Module
Includes perimeter and area methods
"""


class Rectangle:
    """Defining the class and its attributes"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return ((self.__width + self.__height) * 2)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ("")
        for i in range(0, self.__height):
            for j in range(0, self.__width):
                print("#", end="")
            if i != self.__height - 1:
                print("")
        return ("")

    def __repr__(self):
        return ('Rectangle({}, {})'.format(self.__width, self.__height))