from ..lib.linkedlist import LinkedList
import pytest


def test_create_empty_list():
    linked_list = LinkedList()
    assert linked_list.head().value is None


def test_create_list_with_value():
    linked_list = LinkedList("zero")
    assert linked_list.head().value == "zero"


def test_tail_should_return_head():
    linked_list = LinkedList("zero")
    assert linked_list.head() == linked_list.tail()


def test_tail_should_not_be_head():
    linked_list = LinkedList()
    linked_list.append("one")
    linked_list.append("two")
    assert linked_list.head().value != linked_list.tail().value


def test_append_value_to_empty():
    linked_list = LinkedList()
    assert linked_list.head().value is None
    linked_list.append("zero")
    assert linked_list.head().value == "zero"


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


def test_size():
    linked_list = LinkedList()
    assert len(linked_list) == 0
    linked_list.append("zero")
    assert len(linked_list) == 1
    linked_list.append("one")
    assert len(linked_list) == 2


def test_head():
    linked_list = LinkedList("zero")
    assert linked_list.head() == "zero"


def test_tail():
    linked_list = LinkedList("zero")
    assert linked_list.tail() == "zero"
    linked_list.append("one")
    assert linked_list.tail() == "one"


def test_at():
    linked_list = LinkedList("zero")
    linked_list.append("one")
    assert linked_list.at(0) == "zero"
    assert linked_list.at(1) == "one"


def test_pop():
    linked_list = LinkedList("zero")
    linked_list.append("one")
    assert linked_list.tail("one")
    assert linked_list.pop() == "one"
    assert linked_list.tail() == "zeor"


def test_contains():
    linked_list = LinkedList("zero")
    assert linked_list.contains("zero") is True
    assert linked_list.contains("one") is False


def test_find():
    linked_list = LinkedList("zero")
    assert linked_list.find("zero") == "zero"


@pytest.mark.skip("Currently hangs")
def test_to_s():
    linked_list = LinkedList()
    linked_list.append("dog")
    linked_list.append("cat")
    linked_list.append("parrot")
    linked_list.append("hamster")
    linked_list.append("snake")
    linked_list.append("turtle")
    assert (
        linked_list.to_s
        == "( dog ) -> ( cat ) -> ( parrot ) -> ( hamster ) -> ( snake ) -> ( turtle ) -> nil"
    )
