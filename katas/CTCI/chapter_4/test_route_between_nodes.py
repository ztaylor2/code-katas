"""Test route between nodes."""


import pytest


@pytest.fixture
def graph():
    """A graph."""
    from graph import Graph
    return Graph()


def test_empty_graph(graph):
    """Test a graph with two nodes."""
    from route_between_nodes import route_between_nodes
    G = {'a': ['b', 'c'], 'c': ['d']}
    assert route_between_nodes(G, 'a', 'c') is True
