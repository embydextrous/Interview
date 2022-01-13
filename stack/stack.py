# import maxsize from sys module
# Used to return -infinite when stack is empty
from sys import maxsize
 
class Stack:
    def __init__(self):
        self.s = []

    def isEmpty(self):
        return len(self.s) == 0
 
    def push(self, item):
        self.s.append(item)
     
    def pop(self):
        if (self.isEmpty()):
            return str(-maxsize -1) # return minus infinite
        return self.s.pop()
 
    def peek(self):
        if (self.isEmpty()):
            return str(-maxsize -1) # return minus infinite
        return self.s[len(self.s) - 1]

s = Stack()
s.push(20)
s.push(30)
s.push(10)
print(s.pop())
print(s.peek())
print(s.pop())

'''
Other Questions

https://www.geeksforgeeks.org/check-if-stack-elements-are-pairwise-consecutive/
'''