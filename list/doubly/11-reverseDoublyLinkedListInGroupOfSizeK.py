from typing import Counter
from dll import DoublyLinkedList

# Next Question - Sorted Merge of Two Doubly Circular Linked Lists - Break Circle - Sorted Merge - Create Circle

def reverseGroup(node, k):
    current = node
    n = k
    prev, next = None, None
    while current and n > 0:
        n -= 1
        prev, next = current.prev, current.next
        current.next, current.prev = current.prev, current.next
        prev, current = current, next
    if next:
        next.prev = None
        node.next = reverseGroup(next, k)
        node.next.prev = node
    prev.prev = None
    return prev

a = DoublyLinkedList()
for i in range(6):
    a.append(i)
a.print()
a.head = reverseGroup(a.head, 3)
lastNode = a.head
while lastNode.next:
    lastNode = lastNode.next
a.tail = lastNode
a.print()
a.printReverse()
current = a.head
while current:
    print(current.data, current.prev)
    current = current.next
