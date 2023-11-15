#!/usr/bin/python3
"""Defines a string-to-JSON function."""
import json

def to_json_string(my_obj):
    """Return the JSON representation of a string object."""
    try:
        json_string = json.dumps(my_obj)
        return json_string
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
