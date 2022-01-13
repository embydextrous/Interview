from ll import LinkedList, Node

# https://www.geeksforgeeks.org/partitioning-a-linked-list-around-a-given-value-and-keeping-the-original-order/
def rearrange(l, n):
    headA = tailA = Node('*')
    headB = tailB = Node('*')
    headC = tailC = Node('*')
    while l.head:
        if l.head.data == n:
            tailB.next = l.head
            tailB = tailB.next
            l.head, tailB.next = l.head.next, None
        elif l.head.data < n:
            tailA.next = l.head
            tailA = tailA.next
            l.head, tailA.next = l.head.next, None
        else:
            tailC.next = l.head
            tailC = tailC.next
            l.head, tailC.next = l.head.next, None
    headA, headB, headC = headA.next, headB.next, headC.next
    if headA:
        l.head = headA
    elif headB:
        l.head = headB
    else:
        l.head = headC
    if headA:
        if headB:
            tailA.next = headB
            tailB.next = headC
        else:
            tailA.next = headC

a = LinkedList()
a.append(1)
a.append(4)
a.append(3)
a.append(2)
a.append(5)
a.append(2)
a.append(3)
a.print()
rearrange(a, 3)
a.print()