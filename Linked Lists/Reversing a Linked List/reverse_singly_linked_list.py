#!/usr/bin/env python
import unittest


class Node(object):
    """Represents a node in a singly linked list
    Args:
        data: Data to store in a node
    """

    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return "Data: {} Next: {}".format(self.data, bool(self.next))


class LinkedList(object):
    """Represents a singly linked list

    Args:
        *args: List of values for nodes
    """

    def __init__(self, *args):
        self.head = None
        self.tail = None
        for arg in args:
            self.add_last(arg)

    def __str__(self):
        return ",".join(map(str, self.get_list()))

    def add_last(self, data):
        """Inserts at the end of the list"""
        node = Node(data)
        if self.head is None and self.tail is None:
            self.head = node
            self.tail = self.head
        else:
            self.tail.next = node
            self.tail = self.tail.next

    def add_first(self, data):
        """Inserts at the beginning of the list"""
        node = Node(data)
        if self.head is None and self.tail is None:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head = node

    def get_list(self):
        """Print the list"""
        result = []
        current = self.head
        while current != None:
            result.append(current.data)
            current = current.next
        return result

    def reverse(self):
        """Reverses the list"""
        _prev = None
        current = self.head
        self.tail = current
        while current != None:
            _next = current.next
            current.next = _prev
            _prev = current
            current = _next
        self.head = _prev


class TestLinkedList(unittest.TestCase):

    def test_linked_list_reverse(self):
        values = [1, 2, 3, 4, 5]
        linked_list = LinkedList(*values)
        linked_list.reverse()
        reversed_list = linked_list.get_list()
        self.assertEqual(list(reversed(values)), reversed_list)


if __name__ == "__main__":
    unittest.main(verbosity=2)
