from ll import LinkedList, Node

def makeMiddleHead(l):
    if l.head is None or l.head.next is None:
        return
    prev, slow, fast = None, l.head, l.head
    while fast and fast.next:
        fast = fast.next.next
        prev, slow = slow, slow.next
    prev.next = slow.next
    slow.next = l.head
    l.head = slow

a = LinkedList()
for i in range(3):
    a.append(i)
a.print()
makeMiddleHead(a)
a.print()