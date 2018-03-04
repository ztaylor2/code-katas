"""Test queue via stacks."""


import pytest


@pytest.fixture
def q():
    """A queue."""
    from queue_via_stacks import MyQueue
    return MyQueue()


def test_enqueue_and_dequeue(q):
    """Test endque and dequeue work properly."""
    for i in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        q.enqueue(i)

    for i in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        assert q.peek() == i
        assert q.dequeue() == i
