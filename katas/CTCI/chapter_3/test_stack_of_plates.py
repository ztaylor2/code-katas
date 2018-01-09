"""Test stack of plates."""

import pytest


@pytest.fixture
def setofstacks():
    """A set of stacks fixture."""
    from stack_of_plates import SetOfStacks
    return SetOfStacks()


def test_push_and_pop_one_stack(setofstacks):
    """Test push to set of stacks."""
    setofstacks.push(1)
    assert setofstacks.pop() == 1


def test_push_untill_new_stack_created(setofstacks):
    """Test push creates a new stack if at capacity."""
    for i in range(12):
        setofstacks.push(i)
    assert len(setofstacks.stacks) == 2
    assert setofstacks.stacks[0].size() == 10
    assert setofstacks.stacks[0].peek() == 9


def test_pop_method_deletes_stack(setofstacks):
    """Test that the pop method deletes a stack when empty."""
    for i in range(12):
        setofstacks.push(i)
    assert setofstacks.pop() == 11
    assert setofstacks.pop() == 10
    assert len(setofstacks.stacks) == 1
    assert setofstacks.pop() == 9


def test_peek(setofstacks):
    """Test the peek method for a set of stacks."""
    for i in range(12):
        setofstacks.push(i)
    assert setofstacks.peek() == 11
    assert setofstacks.pop() == 11
    assert setofstacks.peek() == 10
    assert setofstacks.pop() == 10
    assert setofstacks.peek() == 9
    assert setofstacks.pop() == 9
