# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 10:34:15 2019

@author: carte
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

            data = self.head.data

            if self.count > 1:
                self.head = self.head.front

            else:
                self.head = None
                self.tail = None

            self.count -= 1
            return data

        else:
            return None


    def is_empty(self):
        if self.head is None and self.tail is None:
            return True
        else:
            return False

    def size(self):
        return self.count


q = Queue()
q.en_queue("a")
q.en_queue("b")
q.en_queue("c")
print(q.count)
print(q.de_queue())
print(q.de_queue())
print(q.de_queue())
q.is_empty()
