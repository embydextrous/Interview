from dll import DoublyLinkedList

def deleteAllOccurences(l, x):
    if l.head is None:
        return
    current = l.head
    while current:
        if current.data == x:
            if current == l.head:
                next = current.next
                current.next = None
                if next:
                    next.prev = None
                l.head = next
                current = l.head
            else:
                prev, next = current.prev, current.next
                current.prev, current.next = None, None
                prev.next = next
                if next:
                    next.prev = prev
                current = next
        else:
            current = current.next

a = DoublyLinkedList()
a.append(2)
a.append(2)
a.append(2)
a.append(2)
a.print()
deleteAllOccurences(a, 2)
a.print()


