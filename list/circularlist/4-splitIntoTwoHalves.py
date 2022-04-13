from cll import CircularLinkedList

def splitIntoTwoHalves(cll):
    if cll.head is None or cll.head == cll.tail:
        return (cll, CircularLinkedList())
    fast, slow = cll.head, cll.head
    while fast.next != cll.head and fast.next.next != cll.head:
        fast = fast.next.next
        slow = slow.next
    nextMid = slow.next
    cll2 = CircularLinkedList()
    cll2.head = nextMid
    cll2.tail = fast if fast == cll.tail else fast.next
    cll2.tail.next = cll2.head
    slow.next = cll.head
    cll.tail = slow
    return (cll, cll2)


a = CircularLinkedList()
a.append(1)
a.append(2)
a.append(3)
a.append(4)
b = splitIntoTwoHalves(a)
b[0].print()
b[1].print()