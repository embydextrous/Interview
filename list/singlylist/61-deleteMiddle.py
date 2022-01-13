from ll import LinkedList, Node

def deleteMiddle(l):
    if l.head is None:
        return
    if l.head.next is None:
        l.head = None
        return
    prevSlow, slow, fast = None, l.head, l.head
    while fast and fast.next:
        fast = fast.next.next
        prevSlow, slow = slow, slow.next
    prevSlow.next = slow.next
    slow.next = None

a = LinkedList()
for i in range(10):
    a.append(i)
a.print()
deleteMiddle(a)
a.print()
deleteMiddle(a)
a.print()
deleteMiddle(a)
a.print()
deleteMiddle(a)
a.print()
deleteMiddle(a)
a.print()
deleteMiddle(a)
a.print()
deleteMiddle(a)
a.print()
deleteMiddle(a)
a.print()
deleteMiddle(a)
a.print()
deleteMiddle(a)
a.print()
deleteMiddle(a)
a.print()