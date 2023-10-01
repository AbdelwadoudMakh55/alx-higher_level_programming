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
        copy_head = self.__head
        if self.__head == None:
            self.__head = Node(value, None)
        else:
            current = self.__head
            previous = current
            while current != None and value > current.data:
                previous = current
                current = current.next_node
            new_node = Node(value, current)
            if previous != current:
                previous.next_node = new_node
            else:
                self.__head = new_node
    def __str__(self):
        list_str = ""
        while self.__head != None:
            if self.__head.next_node == None:
                list_str += str(self.__head.data)
            else:
                list_str += str(self.__head.data) + '\n'
            self.__head = self.__head.next_node
        return f"{list_str}"
