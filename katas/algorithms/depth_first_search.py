"""Depth first search."""


def depth_first_search(node):
    """Preform a depth first search from a node."""
    return_list = []
    visited_nodes = set()

    def dfs(node):
        if node not in visited_nodes:
            return_list.append(node.val)
            visited_nodes.add(node)

        if node.left:
            if node.left not in visited_nodes:
                dfs(node.left)

        if node.right:
            if node.right not in visited_nodes:
                dfs(node.right)

        if node.parent:
            dfs(node.parent)

    dfs(node)

    return return_list
