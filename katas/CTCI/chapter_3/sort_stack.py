"""Sort a stack with just one other stack."""


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


def sort_stack(stack1):
    """Sort a stack."""
    stack2 = Stack()
    while stack1.peek():
        temp = stack1.pop()
        if stack2.peek():
            if temp > stack2.peek():
                stack2.push(temp)
            else:
                count = 0
                while temp < stack2.peek():
                    stack1.push(stack2.pop())
                    count += 1
                stack2.push(temp)
                for _ in range(count):
                    stack2.push(stack1.pop())
        else:
            stack2.push(temp)
    while stack2.peek():
        stack1.push(stack2.pop())
    return stack1
