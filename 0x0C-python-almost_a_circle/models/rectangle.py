#!/usr/bin/python3
"""
Module containing the rectangle class
"""


from .base import Base


class Rectangle(Base):
    """Defining the class rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """getter function for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter function for width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getter function for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter function for height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter function for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter function for x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getter function for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter function for y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """computes rectangle area"""
        return (self.__width * self.__height)

    def display(self):
        """Displays rectangle in stdout"""
        for a in range(self.y):
            print("")
        for i in range(self.height):
            for b in range(self.x):
                print(" ", end="")
            for j in range(self.width):
                print("#", end="")
            print("")

    def update(self, *args, **kwargs):
        """method for updating arguments"""
        if args and len(args) != 0:
            index = 0
            for arg in args:
                if index == 0:
                    self.id == arg
                elif index == 1:
                    self.width = arg
                elif index == 2:
                    self.height = arg
                elif index == 3:
                    self.x = arg
                elif index == 4:
                    self.y = arg
                index += 1
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def __str__(self):
        """Obtain string representation of rectangle objects"""
        return ("[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}"
                .format(self.id, self.x, self.y,
                        self.width, self.height))

    def to_dictionary(self):
        """Dictionary representation of rectangle instances"""
        return ({
                    "id": self.id,
                    "width": self.width,
                    "height": self.height,
                    "x": self.x,
                    "y": self.y
                })
