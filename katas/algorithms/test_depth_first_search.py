"""Test depth first search."""


def test_depth_first_search():
    """Test depth first search."""
    from bst import BinarySearchTree
    from depth_first_search import depth_first_search
    bst = BinarySearchTree([5, 3, 7, 2, 4, 6, 8])
    assert depth_first_search(bst.root) == [5, 3, 2, 4, 7, 6, 8]
