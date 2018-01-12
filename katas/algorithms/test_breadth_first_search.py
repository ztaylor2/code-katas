"""Test breadth first search."""


def test_bfs_returns_correctly():
    """Test bfs with simple tree."""
    from breadth_first_search import breadth_first_search
    from bst import BinarySearchTree
    bst = BinarySearchTree()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    bst.insert(2)
    bst.insert(4)
    bst.insert(6)
    bst.insert(8)
    breadth_output = [5, 3, 7, 2, 4, 6, 8]
    for i in range(len(breadth_output)):
        assert breadth_first_search(bst)[i].val == breadth_output[i]
