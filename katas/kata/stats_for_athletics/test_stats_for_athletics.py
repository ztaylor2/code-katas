"""Test athletic statistics."""

import pytest


STAT_TABLE = [("01|01|01", "Range: 00|00|00 Average: 01|01|01 Median: 01|01|01"),
              ("01|15|59, 1|47|16, 01|17|20, 1|32|34, 2|17|17", "Range: 01|01|18 Average: 01|38|05 Median: 01|32|34"),
              ("02|15|59, 2|47|16, 02|17|20, 2|32|34, 2|17|17, 2|22|00, 2|31|41",
               "Range: 00|31|17 Average: 02|26|18 Median: 02|22|00")]


@pytest.mark.parametrize('n, result', STAT_TABLE)
def test_stats(n, result):
    """Testing stat funciton."""
    from stats_for_athletics import stat
    assert stat(n) == result
