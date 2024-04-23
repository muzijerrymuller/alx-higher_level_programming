#!/usr/bin/python3
"""
Codifies a foundational model class.
"""
class Base:
    """
    Embodies the foundational model.
    """
    __nb_objects = 0
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

