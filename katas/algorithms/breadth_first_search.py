"""A breadth first search in python."""


def breadth_first_search(tree):
    """Breadth first search of a tree."""
    visited_nodes = [tree.root]
    while visited_nodes:
        for node in visited_nodes:
            if node.left:
                visited_nodes.append(node.left)
            if node.right:
                visited_nodes.append(node.right)

    return visited_nodes
