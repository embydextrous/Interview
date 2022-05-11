from collections import deque


class Stack:
    def __init__(self):
        self.q = deque()

    def push(self, data):
        s = len(self.q)
        self.q.append(data)
        for i in range(s):
            self.q.append(self.q.popleft())
        
    def pop(self):
        if len(self.q) == 0:
            return None
        return self.q.popleft()

s = Stack()
for i in range(5):
    s.push(i)
for i in range(5):
    print(s.pop())