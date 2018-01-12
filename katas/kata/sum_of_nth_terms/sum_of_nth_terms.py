"""Sum of the first nth term of Series.

#1 Best Practices Solution:

def series_sum(n):
    return '{:.2f}'.format(sum(1.0/(3 * i + 1) for i in range(n)))

"""


def series_sum(n):
    """Sum to nth num in series."""
    sum = 0
    for i in range(n):
        sum += 1.0 / (1 + 3 * i)
    return '{:.2f}'.format(sum)
