from ll import LinkedList, Node
from random import randint

def segregateEvenOdd(l):
    evenHead = evenTail = Node('*')
    oddHead = oddTail = Node('*')
    current = l.head
    while current:
        if current.data % 2 == 0:
            evenTail.next = current
            evenTail = evenTail.next
        else:
            oddTail.next = current
            oddTail = oddTail.next
        current = current.next
    evenTail.next = None
    oddTail.next = None
    evenHead = evenHead.next
    oddHead = oddHead.next
    if evenHead:
        evenTail.next = oddHead
        l.head = evenHead
    else:
        l.head = oddHead

a = LinkedList()
for i in range(8):
    a.append(randint(1, 20))
a.print()
segregateEvenOdd(a)
a.print()
