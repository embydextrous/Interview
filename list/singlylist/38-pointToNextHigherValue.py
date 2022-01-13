from ll import LinkedList, Node
from random import randint

def findMiddle(node):
    fast, slow = node, node
    while fast.random and fast.random.random:
        fast = fast.random.random
        slow = slow.random
    return slow

def sortedMerge(a, b):
    head = tail = Node('*')
    while a and b:
        if a.data <= b.data:
            tail.random = a
            tail = tail.random
            a = a.random
        else:
            tail.random = b
            tail = tail.random
            b = b.random
    if a:
        tail.random = a
    if b:
        tail.random = b
    return head.random

def mergeSortInternal(node):
    if node is None or node.random is None:
        return node
    middle = findMiddle(node)
    nextMiddle = middle.random
    middle.random = None
    left = mergeSortInternal(node)
    right = mergeSortInternal(nextMiddle)
    return sortedMerge(left, right)

def pointArbitaryToNextHigherValue(a):
    current = a.head
    while current:
        current.random = current.next
        current = current.next
    mergeSortInternal(a.head)


a = LinkedList()
for i in range(6):
    a.append(randint(1, 50))
a.print()
pointArbitaryToNextHigherValue(a)
a.print()
current = a.head
while current:
    print(current.data, current.random.data if current.random else None)
    current = current.next

