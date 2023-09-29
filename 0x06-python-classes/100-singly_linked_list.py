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

class SinglyLinkedList:
    """This the SinglyLinkedList class
    """

    def __init__(self, head=None):
        self.__head = head

    def sorted_insert(self, value):
        if self.__head == None:
            self.__head = Node(value, None)
        else:
            current = self.__head
            while self.__head != None and value > self.__head.data:
                current = self.__head
                self.__head = current.next_node
            if self.__head == None:
                new_node = Node(value, None)
                current.next_node = new_node
            else:
                new_node = Node(value, self.__head)
                current.next_node = new_node
    def printsll(self):
        while self.__head != None:
            print(f"{self.__head.data}")
            self.__head = self.__head.next_node










