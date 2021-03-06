"""Test dijksta algorithm."""


def test_dijksta():
    """."""
    from dijkstra import dijksta
    graph = {'1': [('2', 7), ('3', 9), ('6', 14)],
             '2': [('3', 10), ('4', 15)],
             '3': [('1', 9), ('2', 10), ('6', 2), ('4', 11)],
             '6': [('1', 14), ('3', 2), ('5', 9)],
             '4': [('2', 15), ('3', 11), ('5', 6)],
             '5': [('6', 9), ('4', 6)]
             }

    assert dijksta(graph, '1', '5') == ['1', '3', '6', '5']
