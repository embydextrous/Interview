class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.random = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def append(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            lastNode = self.head
            while lastNode.next:
                lastNode = lastNode.next
            lastNode.next = newNode

    def insertAfter(self, prevNode, data):
        if prevNode is None:
            return
        else:
            newNode = Node(data)
            newNode.next = prevNode.next
            prevNode.next = newNode

    def print(self):
        print("head -> ", end="")
        current = self.head
        while current:
            print(str(current.data) + " -> ", end = "")
            current = current.next
        print("null")

    def printRandom(self):
        print("head -> ", end="")
        current = self.head
        while current:
            print(str(current.data) + " -> ", end = "")
            current = current.random
        print("null")

    def deleteKey(self, key):
        if self.head is None:
            return
        prev, current = None, self.head
        while current:
            if current.data == key:
                break
            prev, current = current, current.next
        if current is None:
            return
        if prev is None:
            self.head = current.next
        else:
            prev.next = current.next
        current.next = None

    def deleteAt(self, index):
        if self.head is None or index < 0:
            return
        prev, current = None, self.head
        while current:
            if index == 0:
                break
            prev, current = current, current.next
            index -= 1
        if current is None:
            return
        if prev is None:
            self.head = current.next
        else:
            prev.next = current.next
        current.next = None

    def delete(self):
        current = self.head
        while current:
            temp = current.next
            self.head = temp
            current.next = None
            current = temp



