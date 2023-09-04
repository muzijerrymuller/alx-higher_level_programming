#!/usr/bin/python3
"""Definition of a Rectangle class."""


class Rectangle:
    """Representation of a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialization of a new Rectangle.

        Args:
            width (integer): The width new rectangle.
            height (integer): The height new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Set the width of said rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an int")
        if value < 0:
            raise ValueError("width must be greater or equal to 0")
        self.__width = value

    @property
    def height(self):
        """Set the height of rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("Height must be an integer")
        if value < 0:
            raise ValueError("Height must be greater or equal to 0")
        self.__height = value
