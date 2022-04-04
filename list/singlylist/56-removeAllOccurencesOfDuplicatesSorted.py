from ll import LinkedList, Node

def removeAllDuplicates(l):
    if l.head is None or l.head.next is None:
        return False
    prev, current, next = None, l.head, l.head.next
    while current and next:
        if current.data == next.data:
            while next.next and next.next.data == current.data:
                next = next.next
            next = next.next
            if prev:
                prev.next = next
            else:
                l.head = next
            if next is None:
                return
            current, next = next, next.next
        else:
            prev, current, next = current, next, next.next

a = LinkedList()
a.append(1)
a.append(1)
a.append(1)
a.append(1)
a.append(75)
a.append(75)
a.print()
removeAllDuplicates(a)
a.print()