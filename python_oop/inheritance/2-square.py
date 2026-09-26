#!/usr/bin/env python3
"""Module for the Square class."""

Square = __import__('1-square').Square


class Square(Square):
    """Represent a square with a string representation."""

    def __str__(self):
        """Return the square description."""
        return "[Square] {}/{}".format(self.__size, self.__size)
