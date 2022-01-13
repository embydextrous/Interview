from cll import CircularLinkedList

def splitIntoTwoHalves(cll):
    if cll.head is None:
        return (cll, cll)
    if cll.head.next is cll.head:
        return (cll, CircularLinkedList())
    fast, prevSlow, slow = cll.head, None, cll.head
    while fast.next != cll.head and fast.next.next != cll.head:
        fast = fast.next.next
        slow = slow.next
    if fast.next == cll.head:
        cll2 = CircularLinkedList()
        cll2.head = slow.next
        slow.next = cll.head
        fast.next = cll2.head
        return (cll, cll2)
    else:
        cll2 = CircularLinkedList()
        cll2.head = slow.next
        slow.next = cll.head
        if fast != slow:
            fast.next.next = cll2.head
        else:
            cll2.head.next = cll2.head
        return (cll, cll2)

a = CircularLinkedList()
a.append(1)
a.append(2)

b = splitIntoTwoHalves(a)
b[0].print()
b[1].print()