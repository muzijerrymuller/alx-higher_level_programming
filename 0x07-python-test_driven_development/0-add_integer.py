#!/usr/bin/python3

"""Definition of an integer add function."""

def add_integer(a, b=98):
    """Returns the integer add of a and b.
    Float arguments are typecasted to int before add is performed.
    Raises:
        TypeError: If either of a or b is a non-integer and non-float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be a integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be a integer")
    return (int(a) + int(b))

