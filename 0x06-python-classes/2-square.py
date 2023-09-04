#!/usr/bin/python3
"""Defines a class Square."""


class Square:
    """Representation of new square."""

    def __init__(self, size=0):
        """Initialization of new Square.
        Args:
            size (int): Size of new square.
        """
        if not isinstance(size, int):
            raise TypeError("Size must be integer")
        elif size < 0:
            raise ValueError("Size must be greater of equal to 0")
        self.__size = size
