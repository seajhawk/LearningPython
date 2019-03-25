# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 13:48:04 2019

@author: Carter Harris
"""
#%%

class Node:
    def __init__(self, data):
       self.data = data
       self.next = None
       
 
class Stack:
    def __init__(self):
        self.head = None
 
    def push(self,data):
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            
    def is_empty(self):
        if self.head is None:
            return(self.head==None)
        else:
            return(self.head==None)
 
    def pop(self):
        if self.head is None:
            return None 
        else:
            popper = self.head.data
            self.head = self.head.next
            return popper
        
    def peek(self):
        if self.head is None:
            return None
        else:
            return self.head.data
        
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.next
        return count
    
stuff = Stack()
stuff.push("fish")
stuff.push("cow")
stuff.push("rock")
stuff.is_empty()
stuff.size()
stuff.peek()
stuff.pop()
stuff.peek()
