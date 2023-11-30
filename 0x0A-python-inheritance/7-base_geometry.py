#!/usr/bin/python3
'''Definition of a base geometry class BaseGeometry.'''

class BaseGeometry:
    '''Reprsentation of base geometry.'''

    def area(self):
        '''Not implemented yet.'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''Validatation of a parameter as an integer.

        Args:
            name (str): The name of parameter.
            value (int): The parameter that is validate.
        Raises:
            TypeError: If value not an integer.
            ValueError: If value is <= 0.
        '''
        if type(value) != int:
            raise TypeError("{} must be integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
