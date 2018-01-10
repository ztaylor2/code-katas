"""Test list of depths."""


def test_list_of_depths():
    """."""
    from list_of_depths import list_of_depths
    from bst import BinarySearchTree
    bst = BinarySearchTree()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    bst.insert(2)
    bst.insert(4)
    bst.insert(5)
    bst.insert(8)
    list_of_lls = list_of_depths(bst)
    assert list_of_lls[0].head.val == 5
