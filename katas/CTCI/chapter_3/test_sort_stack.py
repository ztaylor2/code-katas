"""Test sort stack."""


def test_sort_stack():
    """."""
    from sort_stack import sort_stack
    from sort_stack import Stack
    stack = Stack()
    stack.push(5)
    stack.push(2)
    stack.push(3)
    stack.push(7)
    stack.push(1)
    sorted_stack = sort_stack(stack)
    assert sorted_stack.pop() == 1
    assert sorted_stack.pop() == 2
    assert sorted_stack.pop() == 3
    assert sorted_stack.pop() == 5
    assert sorted_stack.pop() == 7
