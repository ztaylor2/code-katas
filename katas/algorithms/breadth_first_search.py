"""A breadth first search in python."""


def breadth_first_search(tree):
    """Breadth first search of a tree."""
    visited_nodes = [tree.root]
    last_level = [tree.root]
    while last_level:
        next_level = []
        for node in last_level:
            if node.left:
                next_level.append(node.left)
                visited_nodes.append(node.left)
            if node.right:
                next_level.append(node.right)
                visited_nodes.append(node.right)
            last_level = next_level
    return visited_nodes
