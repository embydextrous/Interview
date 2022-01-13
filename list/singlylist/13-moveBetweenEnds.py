from ll import LinkedList, Node

def moveLastToFirst(l):
    if l.head is None:
        return
    prevLast, last = None, l.head
    while last.next:
        prevLast, last = last, last.next
    if prevLast is None:
        return
    prevLast.next = None
    last.next = l.head
    l.head = last

def moveFirstToLast(l):
    if l.head is None or l.head.next is None:
        return
    last = l.head
    while last.next:
        last = last.next
    last.next = l.head
    l.head = l.head.next
    last.next.next = None
    

a = LinkedList()
for i in range(2):
    a.append(i)
a.print()
moveLastToFirst(a)
a.print()
moveFirstToLast(a)
a.print()
    