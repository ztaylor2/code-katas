"""Test post order traversal."""


def test_post_order_traversal():
    """Test post order traversal with simple tree."""
    from bst import BinarySearchTree
    from post_order_traversal import post_order_traversal
    bst = BinarySearchTree([5, 3, 7, 2, 4, 6, 8])
    assert post_order_traversal(bst.root) == [2, 4, 3, 6, 8, 7, 5]
