"""
Partition a list around a given value.

CTCI 2.4
"""

from kth_to_last import LinkedList


def partition_list(linked_list, val):
    """Partition a list around val."""
    greater_nodes = []
    lesser_nodes = []

    current_node = linked_list.head
    while current_node:
        if current_node.data >= val:
            greater_nodes.append(current_node)
        else:
            lesser_nodes.append(current_node)
        current_node = current_node.next

    output_list = LinkedList()
    for node in greater_nodes:
        output_list.push(node.data)

    for node in lesser_nodes:
        output_list.push(node.data)

    return output_list
