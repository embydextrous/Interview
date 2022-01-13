from ll import LinkedList, Node
from random import randint

def findMiddle(node):
    fast, slow = node, node
    while fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next
    return slow

def sortedMerge(a, b):
    head = tail = Node('*')
    while a and b:
        if a.data <= b.data:
            tail.next = a
            tail = tail.next
            a = a.next
        else:
            tail.next = b
            tail = tail.next
            b = b.next
    if a:
        tail.next = a
    if b:
        tail.next = b
    return head.next

def mergeSortInternal(node):
    if node is None or node.next is None:
        return node
    middle = findMiddle(node)
    nextToMiddle = middle.next
    middle.next = None
    left = mergeSortInternal(node)
    right = mergeSortInternal(nextToMiddle)
    return sortedMerge(left, right)

def union(a, b):
    a, b = mergeSortInternal(a), mergeSortInternal(b)
    resultList = LinkedList()
    tail = None
    while a and b:
        if a.data == b.data:
            if tail is None:
                resultList.head = tail = Node(a.data)
            elif tail.data != a.data:
                tail.next = Node(a.data)
                tail = tail.next
            a, b = a.next, b.next
        elif a.data < b.data:
            if tail is None:
                resultList.head = tail = Node(a.data)
            elif tail.data != a.data:
                tail.next = Node(a.data)
                tail = tail.next
            a= a.next
        else:
            if tail is None:
                resultList.head = tail = Node(b.data)
            elif tail.data != b.data:
                tail.next = Node(b.data)
                tail = tail.next
            b = b.next
    while a:
        if tail is None:
            resultList.head = tail = Node(a.data)
        elif tail.data != a.data:
            tail.next = Node(a.data)
            tail = tail.next
        a = a.next
    while b:
        if tail is None:
            resultList.head = tail = Node(b.data)
        elif tail.data != b.data:
            tail.next = Node(b.data)
            tail = tail.next
        b = b.next
    return resultList

def intersection(a, b):
    a, b = mergeSortInternal(a), mergeSortInternal(b)
    resultList = LinkedList()
    tail = None
    while a and b:
        if a.data == b.data:
            if tail is None:
                resultList.head = tail = Node(a.data)
            elif tail.data != a.data:
                tail.next = Node(a.data)
                tail = tail.next
            a, b = a.next, b.next
        elif a.data < b.data:
            a= a.next
        else:
            b = b.next
    return resultList

a = LinkedList()
b = LinkedList()
for i in range(10):
    a.append(randint(1, 20))
    b.append(randint(1, 20))
a.print()
b.print()
intersection(a.head, b.head).print()

