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
    bst.insert(6)
    bst.insert(8)
    list_of_lls = list_of_depths(bst)
    assert list_of_lls[0].head.val == 5
    assert not list_of_lls[0].head.next
    assert list_of_lls[1].head.val == 2
    assert list_of_lls[1].head.next.val == 4
    assert list_of_lls[1].head.next.next.val == 6
    assert list_of_lls[1].head.next.next.next.val == 8
    assert list_of_lls[1].head.next.next.next.next.val == 3
    assert list_of_lls[1].head.next.next.next.next.next.val == 7
    assert list_of_lls[2].head.val == 2
    assert list_of_lls[2].head.next.val == 4
