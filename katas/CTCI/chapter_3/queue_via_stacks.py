"""A queue created with two stacks."""


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
        if self.stack_list:
            return self.stack_list[-1]
        else:
            return None

    def size(self):
        """Return the size of the stack."""
        return self._size


class MyQueue():
    """A queue created with two stacks."""

    def __init__(self):
        """Init the queue."""
        self.stack_1 = Stack()
        self.stack_2 = Stack()

    def enqueue(self, val):
        """Add a value to the queue."""
        while self.stack_1.peek():
            self.stack_2.push(self.stack_1.pop())
        self.stack_1.push(val)
        while self.stack_2.peek():
            self.stack_1.push(self.stack_2.pop())

    def dequeue(self):
        """Remove and return value fom queue."""
        return self.stack_1.pop()

    def peek(self):
        """Peek at the next value to be dequeued."""
        return self.stack_1.peek()
