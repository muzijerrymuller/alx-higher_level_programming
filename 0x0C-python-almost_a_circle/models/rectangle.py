#!/usr/bin/python3
"""
Module for rectangle.
"""
from models.base import Base

class Rectangle(Base):
    """
    Class for Reactangle.
    """
    
    def __init__(self, width, height, x=0, y=0, id=None):

        self.width = width

        self.height = height

        self.x = x

        self.y = y

        super().__init__(id)

        @property
        def width(self):
            return self.__width

        @width.setter
        def width(self, value):
            print(type(value))
            if type(value)is not int:
                raise TypeError("width must be an integer")
            if value <= 0:
                raise ValueError ("width must be > 0")
            self.__width = width

        @property
        def height(self):
            return self.height

        @height.setter
        def height(self, value):
            if type(value) is not int:
                raise TypeError("height must be an integer")
            if value <= 0:
                raise ValueError ("height must be > 0")
            self.__height = height

        @property
        def x(self):
            return self.x

        @x.setter
        def x(self, value):
            if type(value)is not int:
               raise TypeError("x must be an integer")
            if value <= 0:
                raise ValueError ("x must be > 0")
            self.__x = x

        @property
        def y(self):
            return self.y

        @y.setter
        def y(self, value):
            if type(value)is not int:
                raise TypeError("y must be an integer")
            if value <= 0:
                raise ValueError ("y must be > 0")
            self.__y = y

        def area(self):
            area = self.width * self.height
            return area
