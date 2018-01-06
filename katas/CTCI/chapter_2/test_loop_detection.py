"""Test loop detection."""


def test_loop_detection_true():
    """Test when there is a loop."""
    from kth_to_last import LinkedList
    from loop_detection import loop_detection
    test_list = LinkedList()
    test_list.push(1)
    test_list.push(2)
    test_list.push(3)
    test_list.head.next.next = test_list.head.next
    assert loop_detection(test_list) is True


def test_loop_detection_false():
    """Test false where the isn't a loop."""
    from kth_to_last import LinkedList
    from loop_detection import loop_detection
    test_list = LinkedList()
    test_list.push(1)
    test_list.push(2)
    test_list.push(3)
    test_list.push(4)
    assert loop_detection(test_list) is False
