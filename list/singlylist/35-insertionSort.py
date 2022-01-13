from ll import LinkedList, Node
from random import randint

def insertSorted(l, node):
    node.next = None
    if l.head is None:
        l.head = node
        return
    prev, current = None, l.head
    while current:
        if current.data >= node.data:
            break
        prev, current = current, current.next
    if prev is None:
        node.next = l.head
        l.head = node
    else:
        node.next = current
        prev.next = node
    l.print()

def insertionSort(l):
    sortedList = LinkedList()
    while l.head:
        next = l.head.next
        insertSorted(sortedList, l.head)
        l.head = next
    l.head = sortedList.head

a = LinkedList()
for i in range(10):
    a.append(randint(1, 100))
a.print()
insertionSort(a)
a.print()
