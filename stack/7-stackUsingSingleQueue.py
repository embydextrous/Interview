class Stack:
    def __init__(self):
        self.q = []

    def push(self, data):
        s = len(self.q)
        self.q.append(data)
        for i in range(s):
            self.q.append(self.q.pop(0))
        
    def pop(self):
        if len(self.q) == 0:
            return None
        return self.q.pop(0)

s = Stack()
for i in range(5):
    s.push(i)
for i in range(5):
    print(s.pop())