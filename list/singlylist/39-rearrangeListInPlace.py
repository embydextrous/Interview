from ll import LinkedList, Node

# https://www.geeksforgeeks.org/rearrange-a-given-linked-list-in-place/

def findMiddle(node):
    fast, slow = node, node
    while fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next
    return slow

def reverse(node):
    prev, next = None, node
    while node:
        next = node.next
        node.next = prev
        prev, node = node, next
    return prev

def mergeAlternate(a, b):
    head = tail = Node('*')
    while a and b:
        tail.next = a
        tail = tail.next
        a = a.next
        tail.next = b
        tail = tail.next
        b = b.next
    if a:
        tail.next = a
    if b:
        tail.next = b
    return head.next

def arrange(l):
    node = l.head
    if node is None or node.next is None:
        return
    middle = findMiddle(node)
    a = node
    nextToMiddle = middle.next
    middle.next = None
    b = reverse(nextToMiddle)
    l.head = mergeAlternate(a, b)

a = LinkedList()
for i in range(7):
    a.append(i)
a.print()
arrange(a)
a.print()