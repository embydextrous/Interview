from ll import LinkedList, Node

def reverse(l):
    prev, current = None, l.head
    while current:
        next = current.next
        current.next = prev
        prev, current = current, next
    l.head = prev

a = LinkedList()
for i in range(8):
    a.append(i)
a.print()
reverse(a)
a.print()
    