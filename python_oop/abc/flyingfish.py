#!/usr/bin/env python3


class Fish:
    """Represent a fish."""

    def swim(self):
        """Print the swimming behavior of a fish."""
        print("The fish is swimming")

    def habitat(self):
        """Print the habitat of a fish."""
        print("The fish lives in water")


class Bird:
    """Represent a bird."""

    def fly(self):
        """Print the flying behavior of a bird."""
        print("The bird is flying")

    def habitat(self):
        """Print the habitat of a bird."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Represent a flying fish using multiple inheritance."""

    def fly(self):
        """Print the flying behavior of a flying fish."""
        print("The flying fish is soaring!")

    def swim(self):
        """Print the swimming behavior of a flying fish."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Print the habitat of a flying fish."""
        print("The flying fish lives both in water and the sky!")
