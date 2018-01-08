"""Use a single array to implement three stacks.
Methods:
push(stack_num, val)
pop(stack_num)
peek(stack_num)
"""


class ThreeStacks():
    """Three stacks in python."""
    def __init__(self):
        """."""
        self.stack_list = []

    def push(self, stack_num, val):
        """."""
        self.stack_list.append((stack_num, val))
