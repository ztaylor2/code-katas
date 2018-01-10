"""Test linked list."""


import pytest


@pytest.fixture
def ll():
    """A ll."""
    from linked_list import LinkedList
    return LinkedList()


def test_add_method(ll):
    """Test adding to linked list."""
    ll.add(1)
    ll.add(2)
    ll.add(3)
    assert ll.head.val == 3
    assert ll.head.next.val == 2
    assert ll.head.next.next.val == 1
