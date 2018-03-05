"""Check if a bst is balanced at every node."""


def is_balanced(root):
    """Check if balanced."""
    return is_balanced_int(root) >= 0


def is_balanced_int(root):
    """Check if balanced."""
    if root is None:
        return 0
    left = is_balanced_int(root.left)
    right = is_balanced_int(root.right)

    if left < 0 or right < 0 or abs(left - right) > 1:
        return -1
    return max((left, right)) + 1
