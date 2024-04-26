#!/usr/bin/python3
"""
Module for rectangle.
"""

from base import Base

class Reactangle(Base):
    """
    Class for Reactangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
     super().__init__(id)

     self.width = width
     self.height = height
     self.x = x
     self.y

    @property
    def width(self):
         return self.__with

    @width.setter
    def width(self, vlue):
         self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, vlue):
         self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, vlue):
         self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, vlue):
         self.__y = value

