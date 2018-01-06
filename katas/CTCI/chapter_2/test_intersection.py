"""Test list intersection method."""


def test_list_intersection_true():
    """Test when intersection it returns node."""
    from kth_to_last import LinkedList
    from intersection import list_intersection
    list1 = LinkedList()
    list2 = LinkedList()
    list1.push(1)
    list2.push(2)
    list1.head.next = list2.head
    assert list_intersection(list1, list2) == list2.head


def test_list_intersection():
    """Test when no intersection it returns none."""
    from kth_to_last import LinkedList
    from intersection import list_intersection
    list1 = LinkedList()
    list2 = LinkedList()
    list1.push(1)
    list2.push(2)
    assert list_intersection(list1, list2) is None
