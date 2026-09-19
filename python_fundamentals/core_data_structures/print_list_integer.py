#!/usr/bin/env python3
"""Module that prints all integers of a list."""


def print_list_integer(my_list=[]):
    """Print all integers of a list, one per line."""
    for item in my_list:
        print("{:d}".format(item))
