class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.get_value() == other.get_value()
        return self.get_value() == other

    def __str__(self):
        return str(self.value)

    def get_value(self):
        return self.value

    def set_next(self, next_value):
        self.node = Node(next_value)
