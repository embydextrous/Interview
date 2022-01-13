from collections import deque
from typing import Sized

class Queue:
    def __init__(self):
        self.a = []

    def enqueue(self, data):
        self.a.append(data)

    def dequeue(self):
        if len(self.a) == 0:
            return None
        return self.a.pop(0)

class Deque:
    def __init__(self):
        self.a = []

    def enqueueRight(self, data):
        self.a.append(data)

    def enqueueLeft(self, data):
        self.a.insert(0, data)

    def dequeueLeft(self):
        if len(self.a) == 0:
            return None
        return self.a.pop(0)

    def dequeueRight(self):
        if len(self.a) == 0:
            return None
        return self.a.pop()

class StackUsingDeque:
    def __init__(self):
        self.q = deque()

    def push(self, data):
        self.q.append(data)

    def pop(self):
        if len(self.q) == 0:
            return None
        return self.q.pop()

class QueueUsingDeque:
    def __init__(self):
        self.q = deque()

    def enqueue(self, data):
        self.q.append(data)

    def dequeue(self):
        if len(self.q) == 0:
            return None
        return self.q.popleft()

class QueueUsingCircularArray:
    def __init__(self, size):
        self.size = size
        self.a = [None] * size
        self.front = -1
        self.rear = -1

    def enqueue(self, data):
        if (self.rear + 1) % self.size == self.front:
            print("Queue is Full")
            return
        elif self.front == -1:
            self.front = self.rear = 0
            self.a[self.rear] = data
        else:
            self.rear = (self.rear + 1) % self.size
            self.a[self.rear] = data

    def dequeue(self):
        if self.front == -1:
            print("Queue is Empty")
            return
        elif self.front == self.rear:
            v = self.a[self.front]
            self.front = self.rear = -1
            return v
        else:
            v = self.a[self.front]
            self.front = (self.front + 1) % self.size
            return v
