# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 10:34:25 2019

@author: carte
"""

class Node:
    def __init__(self, value):
        self.data = value
        self.front = None
    
    
class Deque:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def isEmpty(self):

    def addFront(self, item):
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

    def addRear(self, item):
        new_node = Node(value)

        if self.tail is not None:
            self.tail.front = new_node

        else:
            self.head = new_node

        self.tail = new_node
        self.count += 1

    def removeFront(self):
        if self.head is None:
            return None
        else:
            removed = self.head.data
            self.head = self.head.next
            self.count -= 1
            return removed

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return self.count
