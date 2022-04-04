from ll import LinkedList, Node
from random import randint
import sys

def reverse(node):
    prev, current = None, node
    while current:
        next = current.next
        current.next = prev
        prev, current = current, next
    return prev

def deleteFromRight(node):
    if node is None:
        return node
    a = reverse(node)
    copyA = a
    maxi = a.data
    while a and a.next:
        if a.next.data > maxi:
            maxi = a.next.data
            a = a.next
        else:
            a.next = a.next.next
    return reverse(copyA)
    

a = LinkedList()
for i in range(10):
    a.append(randint(1,20))
a.print()
a.head = deleteFromRight(a.head)
a.print()
