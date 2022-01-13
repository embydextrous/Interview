from ll import LinkedList, Node

def swapKthNode(l, k):
    c = k - 1
    a, b = l.head, l.head
    prevA, prevB = None, None
    # Find kth node from start and its previous Node
    while a and c > 0:
        prevA, a = a, a.next
        c -= 1
    # Simply means k is greater than length of list
    if a is None:
        return
    d = a
    # Find kth node from end and its previous Node
    while d.next:
        prevB, b, d = b, b.next, d.next
    # no swap required if kth node from beginning and end are same    
    if a == b:
        return
    # swap prev pointers
    if prevA:
        prevA.next = b
    if prevB:
        prevB.next = a
    # swap next pointers
    a.next, b.next = b.next, a.next
    # modify head pointer if required
    if prevA is None:
        l.head = b
    if prevB is None:
        l.head = a


a = LinkedList()
for i in range(9):
    a.append(i)
a.print()
swapKthNode(a, 5)
a.print()