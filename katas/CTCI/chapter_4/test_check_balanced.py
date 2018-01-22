"""Test the check balanced function."""


def test_balanced():
    """."""
    from check_balanced import is_balanced
    from bst import BinarySearchTree
    bst = BinarySearchTree([1, 2, 3, 4, 5])
    assert is_balanced(bst.root) is False


def test_balanced_true():
    """."""
    from check_balanced import is_balanced
    from bst import BinarySearchTree
    bst = BinarySearchTree([5, 3, 7, 2, 4, 6, 8])
    assert is_balanced(bst.root) is True
