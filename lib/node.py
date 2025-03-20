from typing import Any, TypeVar, Generic


T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, value: Any = None, next: T = None) -> None:
        self.value = value
        self.next = next

    def __eq__(self, other) -> bool:
        if isinstance(other, Node):
            return self.get_value() == other.get_value()
        return self.get_value() == other

    def __str__(self) -> str:
        return f"( {str(self.value)} "

    def get_value(self) -> T:
        return self.value

    def set_next(self, next_value: T):
        self.node = Node(next_value)
