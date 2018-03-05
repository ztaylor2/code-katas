"""A stack with push, pop and min methods of O(1) time.

the min method returns the min value in the stack."""


class MinStack():
    """A stack that allows you to return the min value."""

    def __init__(self):
        """Init stack."""
        self.min_val = None
        self.stack_list = []

    def push(self, val):
        """Add a value to the top of the stack."""
        if self.min_val:
            if self.min_val > val:
                self.min_val = val
        else:
            self.min_val = val

        self.stack_list.append(val)

    def min(self):
        """Return the minimum value from the stack."""
        return self.min_val

    def pop(self):
        """Pop value off of stack."""
        if self.stack_list:
            temp_val = self.stack_list[-1]
            self.stack_list.pop()
            if temp_val == self.min_val:
                if self.stack_list:
                    self.min_val = min(self.stack_list)
                else:
                    self.min_val = None
            return temp_val
        else:
            return None
