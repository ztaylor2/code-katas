"""Post order traversal."""


def post_order_traversal(node):
    """A post order traversal."""
    return_list = []

    def post_order(node):
        """Recursive."""
        if node.left:
            post_order(node.left)
        if node.right:
            post_order(node.right)
        return_list.append(node.val)

    post_order(node)
    return return_list
