"""Test tree stacks."""

import pytest


@pytest.fixture
def stack():
    """A stack fixture."""
    from three_in_one import ThreeStacks
    return ThreeStacks()


def test_push_pushes_tuple(stack):
    """Test push method pushes a tuple into the stack lsit."""
    stack.push(1, 1)
    assert stack.stack_list[0] == (1, 1)


def test_push_no_stack_raises(stack):
    """Test push into invalid stack num raises error."""
    with pytest.raises(ValueError):
        stack.push(5, 1)


def test_pop_raises_invalid_stack(stack):
    """Test pup raises error with invalid stack."""
    with pytest.raises(ValueError):
        stack.pop(5)


def test_pop_returns_correct_val(stack):
    """Test pop returns correct val one stack."""
    stack.push(1, 1)
    assert stack.pop(1) == 1
