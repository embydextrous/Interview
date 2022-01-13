from dll import DoublyLinkedList, Node
from random import randint

def findMiddle(node):
    fast, slow = node, node
    while fast.next and fast.next.next:
        fast, slow = fast.next.next, slow.next
    return slow

def merge(a, b):
    head = tail = Node('*')
    while a and b:
        if a.data <= b.data:
            tail.next = a
            a.prev = tail
            tail = tail.next
            a = a.next
        else:
            tail.next = b
            b.prev = tail
            tail = tail.next
            b = b.next
    if a:
        tail.next = a
        a.prev = tail
    if b:
        tail.next = b
        b.prev = tail
    return head.next

def mergeSortInternal(node):
    if node is None or node.next is None:
        return node
    middle = findMiddle(node)
    nextToMiddle = middle.next
    middle.next = None
    if nextToMiddle:
        nextToMiddle.prev = None
    left, right = mergeSortInternal(node), mergeSortInternal(nextToMiddle)
    return merge(left, right)

def mergeSort(l):
    l.head = mergeSortInternal(l.head)

d = DoublyLinkedList()
for i in range(10):
    d.append(randint(1, 99))
d.print()
mergeSort(d)
d.print()
