from ll import LinkedList, Node

def pairwiseSwap(l):
    if l.head is None or l.head.next is None:
        return
    else:
        f, s, t = l.head, l.head.next, l.head.next.next
        f.next = t
        s.next = f
        l.head = s
    prev, node = l.head.next, t
    while node and node.next:
        f, s, t = node, node.next, node.next.next
        f.next = t
        s.next = f
        prev.next = s
        prev = f
        node = t


a = LinkedList()
for i in range(9):
    a.append(i)
a.print()
pairwiseSwap(a)
a.print()