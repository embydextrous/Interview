from cll import CircularLinkedList
#from ll import LinkedList

def exchangeFirstAndLast(l):
    if l.head is None or l.head == l.tail:
        return
    prevLast, last = None, l.head
    while last != l.tail:
        prevLast, last = last, last.next
    prevLast.next = l.head
    last.next = l.head.next
    l.head.next = last
    l.head, l.tail = last, l.head
    
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
