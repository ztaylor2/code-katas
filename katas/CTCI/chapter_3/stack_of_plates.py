"""A set of stacks."""


class Stack():
    """A stack that allows you to return the min value."""

    def __init__(self):
        """Init stack."""
        self.stack_list = []
        self._size = 0

    def push(self, val):
        """Add a value to the top of the stack."""
        self.stack_list.append(val)
        self._size += 1

    def pop(self):
        """Pop value off of stack."""
        self._size -= 1
        return self.stack_list.pop()

    def peek(self):
        """Peek at next value to be popped from stack."""
        return self.stack_list[-1]

    def size(self):
        """Return the size of the stack."""
        return self._size


class SetOfStacks():
    """A set of stacks."""

    def __init__(self, stack_capacity=10):
        """Init set of stacks."""
        self.stack_capacity = stack_capacity
        self._size = 0
        self.stacks = [Stack()]

    def push(self, val):
        """Push a value into set of stacks."""
        if self._size:
            if self._size % self.stack_capacity == 0:
                self.stacks.append(Stack())
        stack_index = self._size // self.stack_capacity
        self.stacks[stack_index].push(val)
        self._size += 1

    def pop(self):
        """Pop a value out of set of stacks."""
        stack_index = self._size // (self.stack_capacity + 1)
        temp_val = self.stacks[stack_index].pop()
        self._size -= 1
        if self._size:
            if self._size % self.stack_capacity == 0:
                self.stacks.pop()
        return temp_val

    def peek(self):
        """Peek at next value to be returned."""
        stack_index = self._size // (self.stack_capacity + 1)
        return self.stacks[stack_index].peek()
