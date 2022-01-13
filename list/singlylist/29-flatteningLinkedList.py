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

def flattenList(node):
    current = node
    s = 0
    while current:
        v = current.v
        current.v = None
        a = current
        while v:
            if a.next:
                if a.next.data >= v.data:
                    next = v.v
                    v.next = a.next
                    a.next = v
                    v.v = None
                    v = next
                    a = a.next
                else:
                    a = a.next
            else:
                a.next = v
                a = a.next
                v = v.v
        s += 1

        current = current.next

def flattenList2(a):
    node = a
    while a:
        if a.v:
            v = a.v
            a.v = None
            a = merge(a, v)
        a = a.next

def merge(a, b):
    head = tail = Node('*')
    while a and b:
        if a.data <= b.data:
            tail.next = a
            a = a.next
            tail = tail.next
        else:
            tail.next = b
            tail = tail.next
            v = b.v
            b.v = None
            b = v
    if a:
        tail.next = a
    while b:
        tail.next = b
        tail = tail.next
        v = b.v
        b.v = None
        b = v
    return head.next
    





a = LinkedList()
a.append(5)
a.append(10)
a.append(19)
a.append(28)
a.head.v = Node(7)
a.head.v.v = Node(8)
a.head.v.v.v = Node(30)

a.head.next.v = Node(20)

a.head.next.next.v = Node(22)
a.head.next.next.v.v = Node(50)

a.head.next.next.next.v = Node(35)
a.head.next.next.next.v.v = Node(40)
a.head.next.next.next.v.v.v = Node(45)

flattenList2(a.head)
a.print()