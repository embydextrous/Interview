from cll import CircularLinkedList
#from ll import LinkedList

def exchangeFirstAndLast(l):
    if l.head is None or l.head.next is l.head:
        return
    prev, current = l.head, l.head.next
    while current.next != l.head:
        prev, current = current, current.next
    current.next = l.head.next
    prev.next = l.head
    l.head.next = current
    l.head = current
    l.tail = prev.next # important we have this otherwise we can accidentaly break CLL
    

#a = LinkedList()
b = CircularLinkedList()

b.append(1)
b.append(2)
b.append(3)
b.append(4)
b.append(5)
b.print()
print(exchangeFirstAndLast(b))
b.print()
