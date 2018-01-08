"""
Use a single array to implement three stacks.

Methods:
push(stack_num, val)
pop(stack_num)
peek(stack_num)
"""


class ThreeStacks():
    """Three stacks in python."""

    def __init__(self):
        """Init stack."""
        self.stack_list = []

    def push(self, stack_num, val):
        """Add a value to a stack."""
        if stack_num not in (1, 2, 3):
            raise ValueError('Enter a valid stack number.')
        self.stack_list.append((stack_num, val))

    def pop(self, stack_num):
        """Pop a value from a specified stack."""
        if stack_num not in (1, 2, 3):
            raise ValueError('Enter a valid stack number.')
        for i in range(len(self.stack_list)):
            if self.stack_list[-(i + 1)][0] == stack_num:
                temp_val = self.stack_list[-(i + 1)][1]
                self.stack_list.pop(-(i + 1))
                return temp_val
        return None

    def peek(self, stack_num):
        """Return next val to be popped from specified stack."""
        if stack_num not in (1, 2, 3):
            raise ValueError('Enter a valid stack number.')
        for i in range(len(self.stack_list)):
            if self.stack_list[-(i + 1)][0] == stack_num:
                return self.stack_list[-(i + 1)][1]
        return None
