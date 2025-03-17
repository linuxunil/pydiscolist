from ..lib.linkedlist import LinkedList


def test_create_empty_list():
    linked_list = LinkedList()
    assert linked_list.head() is None


def test_create_list_with_value():
    linked_list = LinkedList("zero")
    assert linked_list.head() == "zero"


def test_append_value_to_empty():
    linked_list = LinkedList()
    assert linked_list.head() is None
    linked_list.append("zero")
    assert linked_list.head() == "zero"


def test_append_to_unempty():
    linked_list = LinkedList("zero")
    assert linked_list.head() == "zero"
    linked_list.append("one")
    assert linked_list.head() == "zero"
    assert linked_list.tail() == "one"


def test_prepend_to_empty_list():
    linked_list = LinkedList()
    linked_list.prepend("zero")
    assert linked_list.head() == "zero"


def test_prepend_to_list():
    linked_list = LinkedList("zero")
    linked_list.prepend("one")
    assert linked_list.head() == "one"
