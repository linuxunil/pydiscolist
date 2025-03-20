from typing import Any, Iterable

from .node import Node


class LinkedList:
    """A implementation of linked list"""

    class LinkedListIterator:
        def __init__(self, current_node):
            self.current = current_node

        def __iter__(self):
            return self

        def __next__(self):
            if self.current is not None:
                value = self.current.value
                self.current_node = self.current.next
                return value
            else:
                raise StopIteration

    def __init__(self, inital_value: Any | None = None) -> None:
        self.root_node: Node = Node(inital_value)
        # self.size = 1 if inital_value else 0

    def __iter__(self) -> Iterable:
        return self.LinkedListIterator(self.root_node)

    def __str__(self) -> str:
        current_node: Node = self.root_node
        return_str: str = ""
        while current_node:
            return_str += f"( {str(current_node.value)} )"
            return_str += " -> "
            current_node = current_node.next
        return_str += "nil"
        return return_str

    def __len__(self) -> int:
        counter: int = 1
        if (self.root_node.value is None) and (self.root_node.next is None):
            return 0
        elif self.root_node.value is not None and self.root_node.next is None:
            return 1
        else:
            current_node: Node = self.root_node
            while current_node.next:
                current_node = current_node.next
                counter += 1
            return counter

    def at(self, value: int) -> Node:
        current_node: Node = self.root_node
        if value == 0:
            return current_node
        while value != 0:
            current_node = current_node.next
            value -= 1
        return current_node

    def pop(self) -> Node:
        previous_node: Node = self.root_node
        current_node: Node = self.root_node.next
        if self.root_node.next is None:
            self.root_node = Node()
            return previous_node
        while current_node.next:
            previous_node = current_node
            current_node = current_node.next
        previous_node.next = None
        return current_node

    def contains(self, search: Any) -> bool:
        if self.root_node.value == search:
            return True

        current_node: Node = self.root_node

        while current_node.next:
            if current_node.value == search:
                return True
            current_node = current_node.next

        return False

    def find(self, search: Any) -> int | None:
        current_node: Node = self.root_node
        if current_node.value == search:
            return 0
        index: int
        for index in range(len(self)):
            if current_node.value == search:
                return index
            current_node = current_node.next

    def head(self) -> Node:
        return self.root_node

    def tail(self) -> Node:
        current_node: Node = self.root_node
        if self.root_node is None:
            return self.root_node
        while current_node.next:
            current_node = current_node.next

        return current_node

    def prepend(self, value: Any) -> None:
        current_node: Node = self.root_node
        new_node = Node(value)
        self.root_node = new_node
        self.root_node.next = current_node

    def append(self, value: Any) -> None:
        new_node: Node = Node(value)
        current_node: Node = self.root_node
        if current_node.value is None:
            self.root_node = new_node
        else:
            while current_node.next:
                current_node = current_node.next

            current_node.next = new_node
