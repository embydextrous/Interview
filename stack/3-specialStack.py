class SpecialStack:
    def __init__(self):
        self.s = []
        self.minStack = []

    def push(self, data):
        self.s.append(data)
        if len(self.minStack) == 0 or data <= self.getMin():
            self.minStack.append(data)

    def pop(self):
        if len(self.s) == 0:
            return None
        v = self.s.pop()
        if v == self.getMin():
            self.minStack.pop()
        return v

    def getMin(self):
        if len(self.minStack) == 0:
            return None
        return self.minStack[len(self.minStack) - 1]


a = SpecialStack()
a.push(10)
print(a.getMin())
a.push(8)
print(a.getMin())
a.push(12)
print(a.getMin())
a.push(14)
print(a.getMin())
a.push(4)
print(a.getMin())
a.push(3)
print(a.getMin())

a.pop()
print(a.getMin())
a.pop()
print(a.getMin())
a.pop()
print(a.getMin())
a.pop()
print(a.getMin())
a.pop()
print(a.getMin())
a.pop()
print(a.getMin())
a.pop()
print(a.getMin())