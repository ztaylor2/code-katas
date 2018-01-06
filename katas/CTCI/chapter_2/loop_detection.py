"""Detect a loop in a linkedlist."""


def loop_detection(input_list):
    """Check for loop in linked list."""
    runner = input_list.head
    walker = input_list.head
    while runner:
        runner = runner.next.next
        walker = walker.next
        if runner is walker:
            return True
    return False
