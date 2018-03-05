"""Determine if a linked list is a palendrome."""


def linked_palendrome(linked_list):
    """Determine if a linked list is a palendrome."""
    first_half = []
    second_half = []
    i = 0
    current_node = linked_list.head
    while i < linked_list.size() // 2:
        first_half.append(current_node.data)
        current_node = current_node.next
        i += 1

    if linked_list.size() % 2 == 1:
        current_node = current_node.next

    while current_node:
        second_half.append(current_node.data)
        current_node = current_node.next

    for i in range(len(first_half)):
        if first_half[i] != second_half[-(i + 1)]:
            return False
    return True
