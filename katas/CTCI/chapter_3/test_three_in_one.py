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
