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


def test_push_adds_multiple_vals(stack):
    """Test push method adds multiple vals correctly."""
    stack.push(1, 1)
    stack.push(1, 2)
    stack.push(1, 3)
    assert stack.stack_list[0][1] == 1
    assert stack.stack_list[1][1] == 2
    assert stack.stack_list[2][1] == 3


def test_pop_raises_invalid_stack(stack):
    """Test pup raises error with invalid stack."""
    with pytest.raises(ValueError):
        stack.pop(5)


def test_pop_returns_correct_val(stack):
    """Test pop returns correct val one stack."""
    stack.push(1, 1)
    assert stack.pop(1) == 1


def test_pop_deletes_val_from_stack(stack):
    """Test pop deletes value from stack list."""
    stack.push(1, 1)
    stack.pop(1)
    assert len(stack.stack_list) == 0


def test_pop_returns_correct_value_multiple_vals(stack):
    """Test pop returns the correct value when multiple vals pushed in."""
    stack.push(1, 1)
    stack.push(1, 2)
    stack.push(1, 3)
    assert stack.pop(1) == 3


def test_pop_returns_from_correct_stack(stack):
    """Test pop returns from correct stack."""
    stack.push(1, 1)
    stack.push(2, 2)
    stack.push(3, 3)
    assert stack.pop(3) == 3


def test_pop_no_value(stack):
    """Test pop returns no value when empty stack."""
    assert stack.pop(1) is None
