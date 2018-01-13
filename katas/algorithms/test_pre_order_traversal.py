"""Test pre order traversal method."""


def test_pre_order_traversal():
    """Test pre order traversal with simple balanced tree."""
    from pre_order_traversal import pre_order_traversal
    from bst import BinarySearchTree
    bst = BinarySearchTree([5, 3, 7, 2, 4, 6, 8])
    assert pre_order_traversal(bst.root) == [5, 3, 2, 4, 7, 6, 8]
