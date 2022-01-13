from dll import DoublyLinkedList
from random import randint

def sortedInsert(l, node):
    if l.head is None:
        l.head = node
        return
    if l.head.data >= node.data:
        node.next = l.head
        l.head.prev = node
        l.head = node
        return
    current = l.head
    while current.next:
        if current.next.data >= node.data:
            break
        current = current.next
    if current.next is None:
        current.next = node
        node.prev = current
    else:
        node.prev, node.next = current, current.next
        current.next, current.next.prev = node, node


def insertionSort(l):
    result = DoublyLinkedList()
    current = l.head
    while current:
        next = current.next
        current.next = None
        l.head = next
        if next:
            next.prev = None
        sortedInsert(result, current)
        current = next   
    a.head = result.head

a = DoublyLinkedList() 
for i in range(8):
    a.append(randint(1, 25))
a.print()
insertionSort(a)
a.print()
