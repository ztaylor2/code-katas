"""CTCI problem 8.2."""


def robot_paths(grid):
    """Find the number of paths that a robot can take navigating a grid."""
    rows = len(grid)
    cols = len(grid[0])

    def move(j=0, i=0):
        try:
            if grid[i][j] == 0:
                return 0
        except IndexError:
            return 0
        if i == rows - 1 and j == cols - 1:
            return 1

        return move(i - 1, j) + move(i, j + 1)

    return move()
