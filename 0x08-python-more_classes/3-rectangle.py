#!/usr/bin/python3


"""Defines a Rectangle class."""


class Rectangle:
    """Represents a rectangle."""

    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle.

        Args:
            width (int): Width of the new rectangle.
            height (int): Height of the new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Set the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("The width must be an integer")
        if value < 0:
            raise ValueError("The width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Set the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("The height must be an integer")
        if value < 0:
            raise ValueError("The height must be >= 0")
        self.__height = value

    def area(self):
        """it returns the area of the Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """it returns the perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """it return the printable representation of the Rectangle.

        It represents the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))
