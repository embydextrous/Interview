from ll import LinkedList, Node
from random import randint

def reverse(l):
    prev, current = None, l.head
    while current:
        next = current.next
        current.next = prev
        prev, current = current, next
    l.head = prev

def deleteFromRight(l):
    if l.head is None:
        return
    reverse(l)
    maxSoFar = l.head.data
    node = l.head
    while node and node.next:
        next = node.next
        if next.data < maxSoFar:
            node.next = next.next
            next.next = None
        else:
            maxSoFar = next.data
            node = node.next

    reverse(l)

a = LinkedList()
for i in range(100):
    a.append(randint(0,20))
a.print()
deleteFromRight(a)
a.print()
