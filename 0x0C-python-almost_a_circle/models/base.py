#!/usr/bin/python3
"""
Base class of the project
"""


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

        if list_dictionary is None or list_dictionary = []:
            return "[]"
        else:
            return json.dumps(list_dictionary)
