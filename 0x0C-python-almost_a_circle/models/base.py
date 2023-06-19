#!/usr/bin/python3
"""
Base class of the project
"""


import json


class Base:
    """
    base class
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
            Initialisation of class

            Args:
                id (int): id number
        """

        if id is None:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionary):
        """
            returns json string representation of string
        """

        if list_dictionary is None or list_dictionary == []:
            return "[]"
        else:
            return json.dumps(list_dictionary)

    def save_to_file(cls, list_obj):
        """
        """

        name = cls.__name__ + ".json"
        data = []
        if list_obj is not None:
            data = [obj.to_dictionary() for obj in list_dictionary]
            json_data = cls.to_json_string(data)
            with open(name, 'w', encoding="utf-8") as file:
                file.write(json_data)
                
