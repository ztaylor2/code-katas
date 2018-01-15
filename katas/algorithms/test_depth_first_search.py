"""Test depth first search."""


def test_dfs():
    """."""
    from bst import BinarySearchTree
    from depth_first_search import dfs_wrapper
    bst = BinarySearchTree([5, 3, 7, 2, 4, 6, 8])
    assert dfs_wrapper(bst.root) == [5, 3, 2, 4, 7, 6, 8]
