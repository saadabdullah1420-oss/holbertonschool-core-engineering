#!/usr/bin/env python3
"""Module that replaces an element in a list at a specific position."""


def replace_in_list(my_list, idx, element):
    """Replace the element at idx with element, return the list."""
    if idx < 0 or idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list
