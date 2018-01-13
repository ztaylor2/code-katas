"""Test go board method."""


def test_go_board():
    """Test go board method true and false."""
    from go_board import is_captured
    go_board = [
        [None, None, None, None, None, None],
        [None, 1, 1, 0, 0, None],
        [None, 1, 2, 1, 1, None],
        [None, 2, 2, 2, 1, None],
        [None, 2, 1, 1, 1, None],
        [None, None, None, None, None, None],
    ]
    assert is_captured(1, 1, go_board) is False
    assert is_captured(2, 2, go_board) is True
