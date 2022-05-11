from collections import deque

class Stack:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, data):
        self.q2.append(data)
        while len(self.q1) > 0:
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        if len(self.q1) == 0:
            return None
        return self.q1.popleft()

s = Stack()
for i in range(5):
    s.push(i)
for i in range(5):
    print(s.pop())