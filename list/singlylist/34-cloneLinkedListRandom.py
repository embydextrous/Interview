class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.random = None

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

def clone(node):
    resultList = LinkedList()
    resultList.head = tail = Node('*')
    d = {}
    while node:
        next = node.next
        d[node] = next
        tail.next = Node(node.data)
        tail = tail.next
        node.next = tail
        node = next
    for node in d.keys():
        node.next.random = node.random.next
    for node in d.keys():
        node.next = d[node]
    resultList.head = resultList.head.next
    return resultList

def clone2(node):
    resultList = LinkedList()
    if node is None:
        return resultList
    head = node
    while node:
        next = node.next
        copy = Node(node.data)
        node.next, copy.next = copy, next
        node = next     
    o, c, n = head, head.next, head.next.next
    while o:
        c.random = o.random.next
        if n is None:
            break
        o, c, n = n, n.next, n.next.next
    o = head
    c = copyHead = head.next
    print(o.data, c.data)
    while o:
        o.next = o.next.next
        if c.next is None:
            c.next = None
        else:
            c.next = c.next.next
        o, c = o.next, c.next
    resultList.head = copyHead
    return resultList

a = LinkedList()
for i in range(5):
    a.append(i+1)
a.head.random = a.head.next.next
a.head.next.random = a.head
a.head.next.next.random = a.head.next.next.next.next
a.head.next.next.next.random = a.head.next.next
a.head.next.next.next.next.random = a.head.next
a.print()
clonedList = clone2(a.head)
clonedList.print()
node = a.head
while node:
    print(node.random.data)
    node = node.next
a.print()
