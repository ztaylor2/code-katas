"""Test palendrome."""


def test_palendrome_returns_false():
    """Test when not a palendrome."""
    from kth_to_last import LinkedList
    from palendrome import linked_palendrome
    test_ll = LinkedList()
    test_ll.push('a')
    test_ll.push('b')
    test_ll.push('c')
    assert linked_palendrome(test_ll) is False


def test_palendrome_returns_true():
    """Test when a palendrome."""
    from kth_to_last import LinkedList
    from palendrome import linked_palendrome
    test_ll = LinkedList()
    test_ll.push('a')
    test_ll.push('b')
    test_ll.push('a')
    assert linked_palendrome(test_ll) is True


def test_palendrome_even_list_true():
    """Test with even list and true."""
    from kth_to_last import LinkedList
    from palendrome import linked_palendrome
    test_ll = LinkedList()
    test_ll.push('a')
    test_ll.push('b')
    test_ll.push('b')
    test_ll.push('a')
    assert linked_palendrome(test_ll) is True


def test_palendrome_even_list_false():
    """Test with even list and false."""
    from kth_to_last import LinkedList
    from palendrome import linked_palendrome
    test_ll = LinkedList()
    test_ll.push('a')
    test_ll.push('b')
    test_ll.push('c')
    test_ll.push('a')
    assert linked_palendrome(test_ll) is False


def test_palendrome_long_list_true():
    """Test with long list and true."""
    from kth_to_last import LinkedList
    from palendrome import linked_palendrome
    test_ll = LinkedList()
    test_ll.push('a')
    test_ll.push('b')
    test_ll.push('c')
    test_ll.push('d')
    test_ll.push('c')
    test_ll.push('b')
    test_ll.push('a')
    assert linked_palendrome(test_ll) is True
