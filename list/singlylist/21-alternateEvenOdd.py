from ll import LinkedList, Node

def alternateEvenOdd(l):
    odd, even = LinkedList(), LinkedList()
    odd.head, even.head = Node("*"), Node("*")
    oddTail, evenTail = odd.head, even.head
    current = l.head
    while current:
        if current.data % 2 == 0:
            evenTail.next = current
            current = current.next
            l.head = current
            evenTail = evenTail.next
            evenTail.next = None
        else:
            oddTail.next = current
            current = current.next
            l.head = current
            oddTail = oddTail.next
            oddTail.next = None
    odd.head = odd.head.next
    even.head = even.head.next
    l.head = Node("*")
    tail = l.head
    oddc, evenc = odd.head, even.head
    while oddc and evenc:
        nextOdd = oddc.next
        nextEven = evenc.next
        tail.next = oddc
        tail = tail.next
        tail.next = evenc
        tail = tail.next
        oddc, evenc = nextOdd, nextEven
    if oddc:
        tail.next = oddc
    if evenc:
        tail.next = evenc
    l.head = l.head.next


a = LinkedList()
for i in range(8):
    a.append(i)
a.print()
alternateEvenOdd(a)
a.print()