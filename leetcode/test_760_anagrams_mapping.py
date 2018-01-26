"""Test anagrams mapping."""


def test_anagrams_mapping():
    """."""
    from anagrams_mapping import anagram_map
    A = [12, 28, 46, 32, 50]
    B = [50, 12, 32, 46, 28]
    assert anagram_map(A, B) == [1, 4, 3, 2, 0]
