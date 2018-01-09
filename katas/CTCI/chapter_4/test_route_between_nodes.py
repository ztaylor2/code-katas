"""Test route between nodes."""


import pytest


@pytest.fixture
def graph():
    """A graph."""
    from graph import Graph
    return Graph()


def test_simple_graph(graph):
    """Test a graph with two nodes."""
    from route_between_nodes import route_between_nodes
    G = {'a': ['b', 'c'], 'c': ['d']}
    assert route_between_nodes(G, 'a', 'c') is True


def test_false_graph(graph):
    """Test a graph that doesn't have a path."""
    from route_between_nodes import route_between_nodes
    G = {'a': ['b'], 'c': ['d']}
    assert route_between_nodes(G, 'a', 'c') is False


def test_large_graph_true():
    """Test a large graph returns true."""
    from route_between_nodes import route_between_nodes
    G = {'a': ['b', 'c'], 'c': ['d', 'e'], 'e': ['f', 'g', 'h'], 'h': ['z']}
    assert route_between_nodes(G, 'a', 'z')
