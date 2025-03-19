from .node import Node


class LinkedList:
    """A implementation of linked list"""

    class LinkedListIterator:
        def __init__(self, current_node=None):
            self.root_node = current_node

        def __iter__(self):
            return self

        def __next__(self):
            if self.current_node is not None:
                value = self.current_node.value
                self.current_node = self.current_node.next
                return value
            else:
                raise StopIteration

    def __init__(self, inital_value=None):
        self.root_node = Node(inital_value)
        self.size = 1 if inital_value else 0

    def __iter__(self):
        return self.LinkedListIterator(self.root_node)

    def __str__(self):
        return_str = ""
        iterator = self.root_node
        while iterator.next:
            return_str.join(str(iterator.value))

        return return_str

    def head(self):
        return self.root_node

    def tail(self):
        if self.root_node is None:
            return self.root_node
        current_node = self.root_node
        while current_node.next:
            current_node = current_node.next

        return current_node

    def append(self, value):
        new_node = Node(value)
        current_node = self.root_node
        if current_node.value is None:
            self.root_node = new_node
        else:
            while current_node.next:
                current_node = current_node.next

            current_node.next = new_node
