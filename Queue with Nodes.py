# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 10:34:15 2019

@author: carter
"""
class Node:
    def __init__(self, value):
        self.data = value
        self.front = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def en_queue(self, value):
        new_node = Node(value)

        if self.tail is not None:
            self.tail.front = new_node

        else:
            self.head = new_node

        self.tail = new_node
        self.count += 1

    def de_queue(self):
        if not self.is_empty():
            self.head = self.head.front
            self.count -= 1
        else:
            print("Empty")

    def is_empty(self):
        if self.head is None and self.tail is None:
            return True
        else:
            return False

    def size(self):
        return self.count
    

