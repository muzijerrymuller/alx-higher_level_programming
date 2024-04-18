#!/usr/bin/python3

def read_file(filename=""):
    """
    Read and print the content of a text file to stdout.

    Args:
        filename (str): The name of the file to be read. Default is an empty string.

    Returns:
        None
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                print(line, end='')
    except FileNotFoundError as e:
        print(e)
