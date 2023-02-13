#!/usr/bin/python3
"""
Module containing the base class
"""

import json


class Base:
    """This is the base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Class constructor function"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns JSON representation of objects"""
        if list_dictionaries is None:
            return ("[]")
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes JSON representation to a file"""
        filename = cls.__name__ + ".json"
        with open(filename, 'w', encoding="UTF-8") as f:
            if list_objs is None:
                f.write("[]")
            else:
                dict_list = [i.to_dictionary() for i in list_objs]
                f.write(Base.to_json_string(dict_list))

    @staticmethod
    def from_json_string(json_string):
        """returns a list of JSON string representation"""
        if json_string is None:
            return "[]"
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """return instance with all attributes set"""
        if dictionary and len(dictionary) != 0:
            if cls == "Rectangle":
                obj = cls(6, 7, 8)
            else:
                obj = cls(5, 7, 9)
            obj.update(**dictionary)
            return (obj)

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as f:
                dict_list = cls.from_json_string(f.read())
                return [cls.create(**dictionary) for dictionary in dict_list]
        except FileNotFoundError:
            return "[]"
