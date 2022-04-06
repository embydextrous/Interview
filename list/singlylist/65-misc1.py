# https://www.geeksforgeeks.org/maximum-sum-linked-list-two-sorted-linked-lists-common-nodes/
from ll import LinkedList, Node

def maxSumList(a, b):
    sumA, sumB = 0, 0
    head = tail = Node('*')
    headA, headB = a, b
    while a and b:
        if a.data == b.data:
            if sumA >= sumB:
                tail.next = headA
                tail = a
            else:
                tail.next = headB
                tail = b
            a, b = a.next, b.next
            headA, headB = a, b
            sumA, sumB = 0, 0
        elif a.data < b.data:
            sumA += a.data
            a = a.next
        else:
            sumB += b.data
            b = b.next
    while a:
        sumA += a.data
        a = a.next
    while b:
        sumB += b.data
        b = b.next
    if sumA > sumB:
        tail.next = headA
    else:
        tail.next = headB
    return head.next
a = LinkedList()
a.append(1)
a.append(3)
a.append(30)
a.append(90)
a.append(120)
a.append(240)
a.append(511)
b = LinkedList()
b.append(0)
b.append(3)
b.append(12)
b.append(32)
b.append(90)
b.append(125)
b.append(240)
b.append(249)
a.print()
b.print()
c = LinkedList()
c.head = maxSumList(a.head, b.head)
c.print()







