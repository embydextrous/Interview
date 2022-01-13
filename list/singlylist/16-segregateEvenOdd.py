from ll import LinkedList, Node

def segregateEvenOdd(l):
    tail = l.head
    while tail.next:
        tail = tail.next
    prev, current = None, l.head
    firstOddNode = None
    while current and current != firstOddNode:
        if current.data % 2 == 0:
            prev, current = current, current.next
        else:
            if firstOddNode is None:
                firstOddNode = current
            if prev is None:
                l.head = current.next
                tail.next = current
                tail = tail.next
                current.next = None
                current = l.head
            else:
                prev.next = current.next
                tail.next = current
                tail = tail.next
                current.next = None
                current = prev.next

a = LinkedList()
for i in range(8):
    a.append(2*i+1)
a.print()
segregateEvenOdd(a)
a.print()
