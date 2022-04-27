from collections import deque

class Stack:
    def __init__(self):
        self.s = deque()

    def push(self, data):
        self.s.append(data)

    def pop(self):
        if len(self.s) == 0:
            return None
        return self.s.pop()

class Queue:
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
