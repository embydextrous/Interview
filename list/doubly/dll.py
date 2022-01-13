class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.head.prev = newNode
            newNode.next = self.head
            self.head = newNode

    def append(self, data):
        if self.head is None:
            self.push(data)
        else:
            lastNode = self.head
            while lastNode.next:
                lastNode = lastNode.next
            newNode = Node(data)
            lastNode.next = newNode
            newNode.prev = lastNode
            self.tail = newNode

    def insertAfter(self, prevNode, data):
        if self.head is None or prevNode is None:
            return
        newNode = Node(data)
        newNode.prev, newNode.next = prevNode, prevNode.next
        if prevNode.next:
            prevNode.next.prev = newNode
        else:
            self.tail = newNode
        prevNode.next = newNode
    
    def insertBefore(self, nextNode, data):
        if self.head is None or nextNode is None:
            return
        newNode = Node(data)
        newNode.prev, newNode.next = nextNode.prev, nextNode
        if nextNode.prev:
            nextNode.prev.next = newNode
        else:
            self.head = newNode
        nextNode.prev = newNode

    def delete(self, nodeToDelete):
        if self.head is None or nodeToDelete is None:
            return
        if self.head == nodeToDelete:
            self.head = self.head.next
            nodeToDelete.next = None
            if self.head:
                self.head.prev = None
            else:
                self.tail = None
        else:
            prev, next = nodeToDelete.prev, nodeToDelete.next
            nodeToDelete.prev, nodeToDelete.next = None, None
            prev.next = next
            if next:
                next.prev = prev
            else:
                self.tail = prev

    def deleteAt(self, position):
        if self.head is None or position < 0:
            return
        current = self.head
        while current and position > 0:
            position -= 1
            current = current.next
        if current is None:
            return
        if current is self.head:
            next = self.head.next
            current.next = None
            if next:
                next.prev = None
            else:
                self.tail = None
            self.head = next
        else:
            next, prev = current.next, current.prev
            current.next, current.prev = None, None
            prev.next = next
            if next:
                next.prev = prev
            else:
                self.tail = prev
            
    def insertNodeAfter(self, prevNode, newNode):
        if self.head is None or prevNode is None:
            return
        newNode.prev, newNode.next = prevNode, prevNode.next
        if prevNode.next:
            prevNode.next.prev = newNode
        else:
            self.tail = newNode
        prevNode.next = newNode
    
    def insertNodeBefore(self, nextNode, newNode):
        if self.head is None or nextNode is None:
            return
        newNode.prev, newNode.next = nextNode.prev, nextNode
        if nextNode.prev:
            nextNode.prev.next = newNode
        else:
            self.head = newNode
        nextNode.prev = newNode

    def print(self):
        print("head <-> ", end="")
        current = self.head
        while current:
            print(str(current.data) + " <-> ", end = "")
            current = current.next
        print("null")

    def printReverse(self):
        print("null <-> ", end="")
        current = self.tail
        while current:
            print(str(current.data) + " <-> ", end = "")
            current = current.prev
        print("head")


