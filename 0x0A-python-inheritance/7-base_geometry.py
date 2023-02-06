#!/usr/bin/python3
"""
Module containing class BaseGeometry
"""


class BaseGeometry:
    """Empty class"""
    pass

    def area(self):
        """Undefined method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
