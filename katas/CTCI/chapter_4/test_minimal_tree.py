"""Test minimal tree."""


def test_minimal_tree():
    """Test minimal tree with ordered list."""
    from minimal_tree import build_tree
    a_list = [1, 2, 3, 4, 5, 6, 7, 8]
    a_tree = build_tree(a_list)
    assert a_tree.val == 5
