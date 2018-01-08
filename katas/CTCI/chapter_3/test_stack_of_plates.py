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
