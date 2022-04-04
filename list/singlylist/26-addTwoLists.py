from ll import LinkedList, Node

def reverse(l):
    prev, current = None, l.head
    while current:
        next = current.next
        current.next = prev
        prev, current = current, next
    l.head = prev

def add(a, b):
    reverse(a)
    reverse(b)
    sumList = LinkedList()
    nodeA, nodeB = a.head, b.head
    c = 0
    while nodeA and nodeB:
        s = (nodeA.data + nodeB.data + c) % 10
        c = (nodeA.data + nodeB.data + c) // 10
        sumList.push(s)
        nodeA, nodeB = nodeA.next, nodeB.next
    while nodeA:
        s = (nodeA.data + c) % 10
        c = (nodeA.data + c) // 10
        sumList.push(s)
        nodeA = nodeA.next
    while nodeB:
        s = (nodeB.data + c) % 10
        c = (nodeB.data + c) // 10
        sumList.push(s)
        nodeB = nodeB.next
    if c != 0:
        sumList.push(c)
    reverse(a)
    reverse(b)
    return sumList

a = LinkedList()
b = LinkedList()
a.append(9)
a.append(9)
a.append(9)
a.append(4)
a.append(6)

b.append(8)
b.append(4)
a.print()
b.print()
sumList = add(a, b)
a.print()
b.print()
sumList.print()