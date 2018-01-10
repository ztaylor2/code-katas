"""Create a tree of minimal depth from an ordered list."""


class Node():
    """A tree node."""

    def __init__(self, val, left=None, right=None):
        """Init node."""
        self.val = val
        self.left = left
        self.right = right


def build_tree(ordered_list):
    """Build a tree from an ordered list."""
    if not ordered_list:
        return
    mid = len(ordered_list) // 2
    node = Node(ordered_list[mid])
    node.left = build_tree(ordered_list[:mid])
    node.right = build_tree(ordered_list[mid + 1:])
    return node
