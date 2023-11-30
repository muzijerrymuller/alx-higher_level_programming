#!/usr/bin/python3
"""Definition inherited list class MyList."""


class MyList(list):
    """Implementation sorted printing for the built-in list class."""

    def print_sorted(self):
        """Prints a list in sorted ascending order."""
        print(sorted(self))
