"""
CTCI 4.3: Create an algorithm that creates a linked list of all

the nodes at each depth."""


from linked_list import LinkedList


def list_of_depths(tree):
    """Create a LL for each depth in tree."""
    node_children = [tree.root]
    linked_lists = []
    while node_children:
        linked_lists.append(LinkedList([node.val for node in node_children]))
        before_add = len(node_children)
        for node in node_children[::]:
            if node.right:
                node_children.append(node.right)
            if node.left:
                node_children.append(node.left)

        for _ in range(before_add):
            node_children.pop(0)

    return linked_lists
