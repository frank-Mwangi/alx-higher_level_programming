#!/usr/bin/python3
"""
Module containing the class Square
"""


from .rectangle import Rectangle


class Square(Rectangle):
    """Defining attributes of Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """instantiating square objects"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Obtain string representation of square objects"""
        return ("[Square] ({:d}) {:d}/{:d} - {:d}"
                .format(self.id, self.x, self.y, self.width))

    @property
    def size(self):
        """getter method for size"""
        return self.width

    @size.setter
    def size(self, value):
        """setter method for size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """updating arguments method"""
        if args and len(args) != 0:
            index = 0
            for arg in args:
                if index == 0:
                    self.id = arg
                elif index == 1:
                    self.size = arg
                elif index == 2:
                    self.x = arg
                elif index == 3:
                    self.y = arg
                index += 1
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """Dictionary representation of square instances"""
        return ({
                    "id": self.id,
                    "size": self.size,
                    "x": self.x,
                    "y": self.y
                })
