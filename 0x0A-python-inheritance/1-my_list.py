#!/usr/bin/python3
"""MyList class."""

class MyList(list):
    """MyList class."""
    def print_sorted(self):
        """Printing sorted list."""
        for element in sorted(self):
            print(element)
