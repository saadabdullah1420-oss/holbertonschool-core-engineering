#!/usr/bin/env python3
"""Module that updates or adds a key/value pair in a dictionary."""


def update_dictionary(a_dictionary, key, value):
    """Replace key's value if it exists, else create it. Return dict."""
    a_dictionary[key] = value
    return a_dictionary
