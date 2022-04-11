from cll import CircularLinkedList
#from ll import LinkedList

def exchangeFirstAndLast(l):
    # Only one None
    if l.head is None or l.head == l.tail:
        return
    prev, current = l.head, l.head.next
    while current != l.tail:
        prev, current = current, current.next
    prev.next = None
    l.tail.next = None
    l.tail.next = l.head
    l.head, l.tail = current, prev
    
#a = LinkedList()
b = CircularLinkedList()

b.append(1)
b.append(2)
b.append(3)
b.append(4)
b.append(5)
b.append(6)
b.print()
exchangeFirstAndLast(b)
b.print()
