from ll import LinkedList, Node
from random import randint

def alternateEvenOdd(node):
    oddHead = oddTail = Node('*')
    evenHead = evenTail = Node('*')
    while node:
        if node.data % 2 == 0:
            evenTail.next = node
            evenTail = evenTail.next
        else:
            oddTail.next = node
            oddTail = oddTail.next
        node = node.next
    oddTail.next = None
    evenTail.next = None
    oddHead = oddHead.next
    evenHead = evenHead.next
    head = tail = Node('*')
    while oddHead and evenHead:
        tail.next = oddHead
        oddHead = oddHead.next
        tail = tail.next
        tail.next = evenHead
        evenHead = evenHead.next
        tail = tail.next
    if oddHead is None:
        tail.next = evenHead
    if evenHead is None:
        tail.next = oddHead
    return head.next

a = LinkedList()
for i in range(8):
    a.append(randint(1, 20))
a.print()
a.head = alternateEvenOdd(a.head)
a.print()