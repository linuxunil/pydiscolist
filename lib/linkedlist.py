from .node import Node


class LinkedList:
    """A implementation of linked list"""

    def __init__(self, inital_value=None):
        self.root_node = Node(inital_value)
        self.size = 1 if inital_value else 0

    def head(self):
        return self.root_node.value

    def tail(self):
        current_node = self.root_node
        while current_node.next is not None:
            current_node = current_node.next

        return current_node

    def append(self, value):
        current_node = self.root_node
        # If we don't have anything in the list set the root_node to the value
        if self.root_node.next is None:
            self.root_node.value = value
        # Otherwise find the last node and create a new node with the value
        else:
            current_node = self.tail()
            current_node.next = Node(value)
