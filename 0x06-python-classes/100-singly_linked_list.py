#!/usr/bin/python3
"""This the module 100-singly_linked_list for singly linked list.
Classes:
    - 'Node': Class of a singly linked list.
"""
class Node:
    """This is the Node class
    """

    def __init__(self, data, next_node=None):
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        if not isinstance(next_node, Node) and next_node != None:
            raise TypeError("next_node must be a Node object")
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value != None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

    def __str__(self):
        return f"{self.__data}"

class SinglyLinkedList:
    """This the SinglyLinkedList class
    """

    def __init__(self, head=None):
        self.__head = head

    def sorted_insert(self, value):
        if self.__head == None:
            self._head = Node(value, None)
            print(value)
        else:
            while self.__head.next_node != None:
                if value < self.__head.data:
                    self.__head.data = value
                    self.__head.next_node = self.__head.next_node.next_node
                self.__head = self.__head.next_node

    def __str__(self):
        return f"{self.__head}"
