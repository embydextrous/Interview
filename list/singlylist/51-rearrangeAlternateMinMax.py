from ll import LinkedList, Node
from random import randint

def findMiddle(node):
    fast, slow = node, node
    while fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next
    return slow

def reverse(node):
    prev, current = None, node
    while current:
        next = current.next
        current.next = prev
        prev, current = current, next
    return prev

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

def rearrange(l):
    l.head = mergeSortInternal(l.head)
    if l.head is None or l.head.next is None or l.head.next.next is None:
        return
    prevSlow, slow, fast = None, l.head, l.head
    while fast and fast.next:
        fast = fast.next.next
        prevSlow, slow = slow, slow.next
    prevSlow.next = None
    l.print()
    slow = reverse(slow)
    print("ss")
    node = l.head
    while slow:
        next = slow.next
        slow.next = node.next
        node.next = slow
        slow = next
        node = node.next.next

l = LinkedList()
for i in range(10):
    l.append(randint(1, 50))
l.print()
rearrange(l)
l.print()