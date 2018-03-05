"""Test sum lists."""


def test_sum_example():
    """Test sum of two nums."""
    from kth_to_last import LinkedList
    from sum_lists import sum_lists
    list1 = LinkedList()
    list1.push(6)
    list1.push(1)
    list1.push(7)
    list2 = LinkedList()
    list2.push(2)
    list2.push(9)
    list2.push(5)
    sum_list = sum_lists(list1, list2)

    assert sum_list.head.data == 2
    assert sum_list.head.next.data == 1
    assert sum_list.head.next.next.data == 9
