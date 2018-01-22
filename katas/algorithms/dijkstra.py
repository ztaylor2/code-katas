"""Dijkstas shortest path algo."""


def dijksta(graph, start, end):
    """Determine the shortest path from start to end."""
    visited = set()
    distances = {}
    for key in graph:
        distances[key] = (float("inf"), [])

    distances[start] = (0, [start])

    next_nodes = [start]

    while end not in visited:
        current = next_nodes.pop(0)

        for child, edge in graph[current]:
            if child not in visited:
                if distances[child][0] > distances[current][0] + edge:
                    distances[child] = (distances[current][0] + edge, distances[current][1] + [child])
                next_nodes.append(child)

        visited.add(current)

    return distances[end][1]
