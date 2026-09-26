#!/usr/bin/env python3


class VerboseList(list):
    """A list that prints messages when items are added or removed."""

    def append(self, item):
        """Add an item and print a notification."""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, items):
        """Extend the list and print the number of items added."""
        items = list(items)
        super().extend(items)
        print(f"Extended the list with [{len(items)}] items.")

    def remove(self, item):
        """Remove an item and print a notification."""
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """Remove and return an item with a notification."""
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
