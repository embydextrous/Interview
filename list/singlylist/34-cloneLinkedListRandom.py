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
    if node is None:
        return None
    originalHead = node
    while node:
        copyNode = Node(node.data)
        copyNode.next = node.next
        node.next = copyNode
        node = node.next.next
    node = originalHead
    while node:
        if node.random:
            node.next.random = node.random.next
        node = node.next.next
    node = originalHead
    copyHead = originalHead.next
    while node:
        copyNode = node.next
        node.next = copyNode.next 
        node = node.next
        if node:
            copyNode.next = node.next
    return copyHead           

a = LinkedList()
for i in range(5):
    a.append(i+1)
a.head.random = a.head.next.next
a.head.next.random = a.head
a.head.next.next.random = a.head.next.next.next.next
a.head.next.next.next.random = a.head.next.next
a.head.next.next.next.next.random = a.head.next
a.print()
clonedList = LinkedList()
clonedList.head = clone(a.head)
a.print()
clonedList.print()
node = a.head
copyNode = clonedList.head
while node and copyNode:
    print(node.random.data, copyNode.random.data)
    node = node.next
    copyNode = copyNode.next
a.print()
