class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.v = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            lastNode = self.head
            while lastNode.next:
                lastNode = lastNode.next
            lastNode.next = newNode

    def print(self):
        print("head -> ", end="")
        current = self.head
        while current:
            print(str(current.data) + " -> ", end = "")
            current = current.next
        print("null")

def flattenMultilevelList(node):
    lastNode = node
    while lastNode.next:
        lastNode = lastNode.next
    while node:
        if node.v:
            v = node.v
            node.v = None
            lastNode.next = v
            while lastNode.next:
                lastNode = lastNode.next
        node = node.next

a = LinkedList()
a.append(10)
a.append(5)
a.append(12)
a.append(7)
a.append(11)

a.head.v = Node(4)
a.head.v.next = Node(20)
a.head.v.next.next = Node(13)
a.head.v.next.next.v = Node(16)
a.head.v.next.next.v.v = Node(3)

a.head.v.next.v = Node(2)

a.head.next.next.next.v = Node(17)
a.head.next.next.next.v.next = Node(6)

a.head.next.next.next.v.v = Node(9)
a.head.next.next.next.v.v.next = Node(8)

a.head.next.next.next.v.v.v = Node(19)
a.head.next.next.next.v.v.v.next = Node(15)

flattenMultilevelList(a.head)
a.print()




