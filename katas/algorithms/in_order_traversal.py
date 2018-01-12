"""In order traversal."""


def in_order_traversal(node):
    """An in order traversal."""
    visited = set()
    return_list = []

    def in_order(node):
        """."""
        if not node.right and not node.left:
            return_list.append(node.val)
            visited.add(node)
            in_order(node.parent)
        if node.left and node.left not in visited:
            in_order(node.left)
        if node.right and node.right not in visited:
            visited.add(node)
            return_list.append(node.val)
            in_order(node.right)

        if node.right in visited and node.left in visited:
            if node.parent:
                in_order(node.parent)

    in_order(node)
    return return_list
