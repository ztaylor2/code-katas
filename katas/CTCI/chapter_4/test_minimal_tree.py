"""Test minimal tree."""


def test_minimal_tree():
    """Test minimal tree with ordered list."""
    from minimal_tree import build_tree
    a_list = [1, 2, 3, 4, 5, 6, 7, 8]
    a_tree = build_tree(a_list)
    assert a_tree.val == 5
    assert a_tree.right.val == 7
    assert a_tree.left.val == 3
    assert a_tree.left.left.val == 2
    assert a_tree.left.right.val == 4
    assert a_tree.right.left.val == 6
    assert a_tree.right.right.val == 8
    assert a_tree.left.left.left.val == 1
