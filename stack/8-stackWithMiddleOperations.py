# https://www.geeksforgeeks.org/design-a-stack-with-find-middle-operation/

class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.mid = None
        self.count = 0

    def push(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.count += 1
        if self.count == 1:
            self.mid = newNode
        else:
            self.head.prev = newNode
            if self.count % 2 != 0:
                self.mid = self.mid.prev
        self.head = newNode

    def pop(self):
        if self.count == 0:
            print("Stack is empty")
            return None
        node = self.head
        self.count -= 1
        if self.count == 0:
            self.head, self.mid = None, None
        else:
            next = node.next
            node.prev = None
            node.next = None
            self.head = next
            if self.count % 2 == 0:
                self.mid = self.mid.next
        return node.data

    def getMiddle(self):
        if self.mid is None:
            print("Stack is empty")
            return None
        return self.mid.data

s = Stack()
s.push(1)
print(s.getMiddle())
s.push(2)
print(s.getMiddle())
s.push(3)
print(s.getMiddle())
s.push(4)
print(s.getMiddle())
s.push(5)
print(s.getMiddle())
s.deleteMiddle()
print(s.getMiddle())
s.deleteMiddle()
print(s.getMiddle())
s.deleteMiddle()
print(s.getMiddle())


