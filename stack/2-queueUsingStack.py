class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enqueue(self, data):
        self.s1.append(data)

    # expensive dequeue operation - better for write heavy queues
    def dequeue(self):
        if len(self.s1) == 0:
            return None
        while len(self.s1) > 0:
            self.s2.append(self.s1.pop())
        v = self.s2.pop()
        while len(self.s2) > 0:
            self.s1.append(self.s2.pop())
        return v

class Queue2:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enqueue(self, data):
        while len(self.s1) > 0:
            self.s2.append(self.s1.pop())
        self.s2.append(data)
        while len(self.s2) > 0:
            self.s1.append(self.s2.pop())

    # expensive dequeue operation - better for write heavy queues
    def dequeue(self):
        if len(self.s1) == 0:
            return None
        return self.s1.pop()


q = Queue2()
q.enqueue(23)
q.enqueue(26)
q.enqueue(12)
q.enqueue(8)
q.enqueue(9)

print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())