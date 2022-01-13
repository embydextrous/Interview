import sys

class SpecialStack:
    def __init__(self):
        self.s = []
        self.min = sys.maxsize

    def push(self, data):
        if data < self.min:
            self.s.append(2 * data - self.min) # if data < self.min, then 2*data - self.min < self.min, store 2 * data - self.min in stack and data to self.min
            self.min = data
        else:
            self.s.append(data)

    def pop(self):
        if len(self.s) == 0:
            return None
        v = self.s.pop()
        if len(self.s) == 0:
            self.min = sys.maxsize
            return v
        if v < self.getMin():
            v, self.min = self.min, 2 * self.min - v # clearly the element here to pop is self.min, to construct new min make reverse query
        return v
        

    def getMin(self):
        return self.min


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