"""Test partition list."""


def test_partition_list_short_list():
    """Test partition a short list around a val."""
    from kth_to_last import LinkedList
    from partition_list import partition_list
    test_ll = LinkedList()
    test_ll.push(1)
    test_ll.push(2)
    test_ll.push(3)
    partitioned_list = partition_list(test_ll, 2)
    assert partitioned_list.head.data == 1
    assert partitioned_list.head.next.data == 2
    assert partitioned_list.head.next.next.data == 3
