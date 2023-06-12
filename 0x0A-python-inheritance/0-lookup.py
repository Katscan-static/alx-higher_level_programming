#!/usr/bin/python3

def lookup(obj):
    """
        A funtion that return the attributes of a function.

        Args:
        obj (class): a class object

        Returns: a dictionary of all attributes
    """
    return obj.__dict__
