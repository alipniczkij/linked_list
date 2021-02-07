import pytest
from linked_list.linked_list import LinkedList, Node

def test_linked_list_01():
    ll = LinkedList([1, 2, 3])

    assert ll.head is not None
    assert ll.head.el == 1
    assert ll.end is not None
    assert ll.end.el == 3
    assert ll.head.next is not None
    assert ll.head.next.el == 2
    assert ll.head.next.next is not None
    assert ll.head.next.next.el == 3

def test_linked_list_02():
    ll = LinkedList()

    ll.append(10)
    assert ll.head is not None
    assert ll.head.el == 10
    assert ll.head.next is None
    assert ll == LinkedList([10])

    ll.append(11)
    assert ll.head.next == Node(11)
    assert ll.head.next.el == 11
    assert ll.end.el == 11

def test_linked_list_03():
    assert LinkedList([1, 2, 3, 4, 5]).count() == 5
    assert len(LinkedList([1, 2, 3, 4, 5])) == 5

def test_linked_list_04():
    ll = LinkedList([1, 2, 3])

    elem = ll.pop()
    assert elem == 3
    assert ll.end.el == 2
    assert ll == LinkedList([1, 2])

    first = ll.pop(0)
    assert first == 1
    assert ll.head.el == 2
    assert len(ll) == 1
    assert ll == LinkedList([2])

    ll.append(3)
    ll.append(4)

    middle = ll.pop(1)
    assert middle == 3
    assert ll.head.next.el == 4
    assert ll == LinkedList([2, 4])

    ll.pop()
    ll.pop()

    assert ll == LinkedList()
    assert ll.head is None
    assert len(ll) == 0

    with pytest.raises(IndexError):
        ll.pop()

def test_linked_list_05():
    ll = LinkedList([1, 2, 3])

    assert ll[1] == 2
    with pytest.raises(IndexError):
        ll[3]

def test_linked_list_06():
    ll = LinkedList([1, 2, 3])

    new_ll = ll + LinkedList([4, 5])
    assert new_ll == LinkedList([1, 2, 3, 4, 5])

    new_ll = new_ll + LinkedList()
    assert new_ll == LinkedList([1, 2, 3, 4, 5])

    new_ll = LinkedList() + new_ll
    assert new_ll == LinkedList([1, 2, 3, 4, 5])

    ll_1 = LinkedList()
    ll_2 = ll_1 + LinkedList()
    assert len(ll_2) == 0

    ll_1 += LinkedList([1])
    assert len(ll_1) == 1

def test_linked_list_07():
    ll = LinkedList([1, 2, 3])

    assert str(ll) == "[1, 2, 3]"
    assert str(LinkedList())