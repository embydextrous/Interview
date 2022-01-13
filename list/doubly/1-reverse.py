from dll import DoublyLinkedList

def reverse(dll):
    current = dll.head
    while current:
        current.next, current.prev = current.prev, current.next
        if current.prev is None:
            break
        current = current.prev
    dll.head = current

a = DoublyLinkedList()
for i in range(8):
    a.append(i)
a.print()
reverse(a)
a.print()