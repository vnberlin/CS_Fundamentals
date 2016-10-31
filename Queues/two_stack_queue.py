#!/usr/bin/python
# Filename: two_stack_queue.py
""" This implementation of a Queue Data Structure using 2 Stack Data structures"""
__author__ = "vnberlin"


class Stack:
    def __init__(self, size):
        self.size = size
        self.lst = []

    def push(self, data):
        if len(self.lst) < self.size:
            self.lst.append(data)
            return True
        else:
            return False

    def pop(self):
        return self.lst.pop()

    def get_size(self):
        return self.size

    def isEmpty(self):
        return self.lst == []


class Queue:
    def __init__(self, size):
        self.size = size
        self.instack = Stack(self.size)
        self.outstack = Stack(self.size)

    def enqueue(self, data):
        t = self.instack.push(data)
        if t:
            print "queued data : %d" % data
        else:
            print "error: queue full"

    def dequeue(self):
        if self.instack.isEmpty() and self.outstack.isEmpty():
            print "queue empty"
        elif self.outstack.isEmpty() and not (self.instack.isEmpty()):
            while (not self.instack.isEmpty()):
                self.outstack.push(self.instack.pop())
            return self.outstack.pop()
        else:
            return self.outstack.pop()

    def __private_order_queue(self):
        pass
        # its possible to use both stacks more efficiently to use memory more efficiently
        # it can allow you queue more double the data eg q = Queue(5) can queue 10 items
        # if you move line 40 and 41 here and call this private method from dequeue method

# End of two_stack_queue.py
