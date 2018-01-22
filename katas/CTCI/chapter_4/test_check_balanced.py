"""Test the check balanced function."""


def test_balanced():
    """."""
    from check_balanced import is_balanced
    from bst import BinarySearchTree
    bst = BinarySearchTree([1, 2, 3, 4, 5])
    assert is_balanced(bst.root) is False
