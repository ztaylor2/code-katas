"""A method that removes duplicates from a linked list."""


class Node(object):
    """The node object."""

    def __init__(self, data, next):
        """Build node attributes on init."""
        self.data = data
        self.next = next


class LinkedList(object):
    """Create linked list object."""

    def __init__(self, iterable=None):
        """Head node is none on init."""
        self.head = None
        self._counter = 0
        if isinstance(iterable, (tuple, list)):
            for item in iterable:
                self.push(item)

    def push(self, data):
        """Push value to linked list."""
        if isinstance(data, (tuple, list)):
            for item in data:
                new_node = Node(item, self.head)
                self.head = new_node
                self._counter += 1
        else:
            new_node = Node(data, self.head)
            self.head = new_node
            self._counter += 1

    def pop(self):
        """Remove first item from list and return it."""
        if not self.head:
            raise IndexError("List is empty.")
        output = self.head.data
        self.head = self.head.next
        self._counter -= 1
        return output

    def size(self):
        """Return the size of the linked list."""
        return self._counter

    def search(self, val):
        """Search for a node in the linked list."""
        curr = self.head
        while curr:
            if curr.data == val:
                return curr
            curr = curr.next

    def display(self):
        """Display the linked list."""
        output_string = "("
        node = self.head
        if node is None:
            return '()'
        while node:
            try:
                float(node.data)
                output_string += (str(node.data) + ", ")
            except ValueError:
                output_string += ("\'" + node.data + "\'") + ", "
            node = node.next
        output_string = output_string[:-2] + ')'
        return(output_string)

    def __len__(self):
        """Return size of linked list."""
        return self._counter

    def remove(self, node):
        """Remove an item from the linked list."""
        current_node = self.head
        previous_node = None
        while current_node:
            if current_node.data == node:
                if previous_node is None:
                    self.head = current_node.next
                    self._counter -= 1
                    return
                else:
                    previous_node.next = current_node.next
                    self._counter -= 1
                    return
            else:
                previous_node = current_node
                current_node = current_node.next
        raise IndexError('Node not in linked list.')

    def remove_dupes(self):
        """Remove any duplicates in the linked list."""
        if self._counter == 0 or self._counter == 1:
            return
        current_node = self.head
        while current_node:
            next_node = current_node.next
            previous_node = current_node
            while next_node:
                if next_node.data == current_node.data:
                    previous_node.next = next_node.next
                    next_node = next_node.next
                    self._counter -= 1
                    continue
                previous_node = next_node
                next_node = next_node.next
            current_node = current_node.next

    def __str__(self):
        """Return what the display method returns."""
        return self.display()
