"""Detect an intersection in two linked lists."""


def list_intersection(list1, list2):
    """Check for list intersection."""
    list1_nodes = {}

    curr_node1 = list1.head
    while curr_node1:
        list1_nodes[curr_node1] = True
        curr_node1 = curr_node1.next

    curr_node2 = list2.head
    while curr_node2:
        if curr_node2 in list1_nodes:
            return curr_node2
        curr_node2 = curr_node2.next

    return None
