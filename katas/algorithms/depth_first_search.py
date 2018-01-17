"""Depth first search."""


def dfs_wrapper(node):
    """."""
    dfs_vals = []

    def dfs(node):
        """."""
        dfs_vals.append(node.val)
        if node.left:
            dfs(node.left)
        if node.right:
            dfs(node.right)
    dfs(node)
    return dfs_vals
