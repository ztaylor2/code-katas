"""Sum of all multiples of 3 or 5 less than 1000."""


def determine_sum_of_multiples():
    """Sum of all multiples of 3 or 5 less than 1000."""
    sum_of_multiples = 0
    for i in range(1000):
        if (i % 3 == 0 or i % 5 == 0):
            sum_of_multiples = sum_of_multiples + i
    return sum_of_multiples


def test_sum_3_5():
    """Test the algo."""
    from sum_3_5 import determine_sum_of_multiples
    assert determine_sum_of_multiples() == 233168
