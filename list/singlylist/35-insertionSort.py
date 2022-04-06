from ll import LinkedList, Node
from random import randint

def insertSorted(head, node):
    prev, current = None, head
    while current:
        if current.data > node.data:
            break
        prev, current = current, current.next
    if prev:
        node.next = prev.next
        prev.next = node
        return head
    else:
        node.next = head
        return node

def insertionSort(head):
    if head is None:
        return
    node = head.next
    head.next = None
    while node:
        next = node.next
        head = insertSorted(head, node)
        node = next
    return head

a = LinkedList()
for i in range(10):
    a.append(randint(1, 100))
a.print()
a.head = insertionSort(a.head)
a.print()
