"""In order traversal."""


def in_order_traversal(node):
    """An in order traversal."""
    return_list = []

    def in_order(node):
        """Recursive."""
        if node.left:
            in_order(node.left)
        return_list.append(node.val)
        if node.right:
            in_order(node.right)

    in_order(node)
    return return_list
