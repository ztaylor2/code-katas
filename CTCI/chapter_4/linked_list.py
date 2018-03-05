"""A linked list in python."""


class Node():
    """A linked list node."""

    def __init__(self, val, next=None):
        """Init node."""
        self.val = val
        self.next = next


class LinkedList():
    """A linked list."""

    def __init__(self, vals=None):
        """Init linked list."""
        self.head = None
        if isinstance(vals, list):
            for val in vals:
                self.add(val)

    def add(self, val):
        """Add a value to the linked list."""
        self.head = Node(val, self.head)
