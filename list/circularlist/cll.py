#3 - Convert Singly List to Circular List - if empty do nothing, else find last node and connect to head

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

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
        prev, current = None, self.head
        while current.next != self.head:
            if current == nodeToDelete:
                break
            prev, current = current, current.next
        if prev:
            prev.next = current.next
            current.next = None
        else:
            lastNode = self.head
            while lastNode.next != self.head:
                lastNode = lastNode.next
            lastNode.next = self.head.next
            self.head = lastNode.next


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
