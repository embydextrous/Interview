#3 - Convert Singly List to Circular List - if empty do nothing, else find last node and connect to head

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            newNode.next = newNode
        else:
            self.tail.next = newNode
            newNode.next = self.head
            self.head = newNode

    def append(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            newNode.next = newNode
        else:
            newNode.next = self.head
            self.tail.next = newNode
            self.tail = newNode

    def delete(self, nodeToDelete):
        if self.head is None:
            return
        if nodeToDelete == self.head:
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                nextHead = self.head.next
                self.head.next = None
                self.head = nextHead
                self.tail.next = nextHead
        else:
            prev, current = None, self.head
            while current != nodeToDelete:
                prev, current = current, current.next
            prev.next = current.next
            current.next = None
            if nodeToDelete == self.tail:
                self.tail = prev

    def print(self):
        print("head -> ", end="")
        current = self.head
        while current and True:
            print(str(current.data) + " -> ", end = "")
            current = current.next
            if current == self.head:
                break
        print("head")

a = CircularLinkedList()
a.push(1)
a.push(2)
a.append(3)
a.delete(a.head.next.next.next)
#print(a.head.data, a.tail.data)
#a.print()
