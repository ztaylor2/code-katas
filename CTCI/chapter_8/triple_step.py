"""CTCI problem 8.1."""


def triple_step(n):
    """Count number of ways boy can run up steps."""
    def count_step(steps):
        if steps == n:
            return 1
        if steps > n:
            return 0
        return count_step(steps + 1) + count_step(steps + 2) + count_step(steps + 3)

    return count_step(0)
