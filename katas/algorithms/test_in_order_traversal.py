"""Test in order traversal method."""


def test_in_order_traversal():
    """Test in order traversal with simple balanced tree."""
    from in_order_traversal import in_order_traversal
    from bst import BinarySearchTree
    bst = BinarySearchTree([5, 3, 7, 2, 4, 6, 8])
    assert in_order_traversal(bst.root) == [2, 3, 4, 5, 6, 7, 8]
