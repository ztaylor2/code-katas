"""Pre order traversal."""


def pre_order_traversal(node):
    """A pre order traversal."""
    return_list = []

    def pre_order(node):
        """Recursive."""
        return_list.append(node.val)
        if node.left:
            pre_order(node.left)
        if node.right:
            pre_order(node.right)

    pre_order(node)
    return return_list
