"""Determine if there is a route between two nodes in a weighted graph."""


def route_between_nodes(graph, a, b):
    """Determine if there is a route between two nodes."""
    if breadth_first(graph, a, b) is True:
        return True
    if breadth_first(graph, b, a) is True:
        return True
    return False


def breadth_first(graph, start, finish):
    """Breadth first search."""
    children_nodes = [start]
    visited = []
    while children_nodes:
        if children_nodes[0] in graph:
            for child in graph[children_nodes[0]]:
                if child == finish:
                        return True
                if children_nodes not in visited:
                    children_nodes.append(child)
                visited.append(child)
        children_nodes.pop(0)
    return False
