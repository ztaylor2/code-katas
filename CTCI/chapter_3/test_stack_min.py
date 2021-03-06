"""Test min stack."""


import pytest


@pytest.fixture
def stack():
    """A stack."""
    from stack_min import MinStack
    return MinStack()


def test_push_and_pop_methods(stack):
    """Test the push method."""
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.pop() == 3
    assert stack.pop() == 2
    assert stack.pop() == 1


def test_min_method(stack):
    """Test the min method returns min value."""
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    assert stack.min() == 1


def test_min_after_popping_min(stack):
    """Test return min value after popping min val."""
    stack.push(5)
    stack.push(7)
    stack.push(43)
    stack.push(4)
    assert stack.min() == 4
    assert stack.pop() == 4
    assert stack.min() == 5
