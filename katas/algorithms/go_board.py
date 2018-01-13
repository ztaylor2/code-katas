"""Determine if a piece is captured on a go board.

0 = empty
1 = while
2 = black
None = edge

ex:
    go_board = [
        [None, None, None, None, None, None],
        [None, 1, 1, 0, 0, None],
        [None, 1, 2, 1, 1, None],
        [None, 2, 2, 2, 1, None],
        [None, 2, 1, 1, 1, None],
        [None, None, None, None, None, None],
    ]

if input is at location of any two, should return True

if input is at location of any one, should return False

"""


def is_captured(i, j, go_board):
    """Determine if a given piece is captured on a go board."""
    visited = set()
    to_visit = [(i, j)]

    while to_visit:
        visited.add(to_visit[0])
        x, y = to_visit.pop(0)
        pots = [(x + a[0], y + a[1]) for a in ((0, 1), (0, -1), (1, 0), (-1, 0))]
        for pot in pots:
            if go_board[pot[0]][pot[1]] == 0:
                return False
            elif go_board[pot[0]][pot[1]] == go_board[i][j] and pot not in visited:
                to_visit.append(pot)
    return True
