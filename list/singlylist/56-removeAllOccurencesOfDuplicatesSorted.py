from ll import LinkedList, Node

def removeAllDuplicates(l):
    prev, current = None, l.head
    while current:
        next = current.next            
        if next and current.data == next.data:
            current = next
        else:
            if prev is None:
                if current != l.head:
                    l.head = next
                    current.next = None
                    current = next
                else:
                    prev, current = current, next
            else:
                if current != prev.next:
                    prev.next = next
                    current.next = None
                    current = next
                else:
                    prev, current = current, next

a = LinkedList()
a.append(1)
#a.append(1)
a.append(1)
a.append(1)
#a.append(75)
#a.append(75)
a.print()
removeAllDuplicates(a)
a.print()