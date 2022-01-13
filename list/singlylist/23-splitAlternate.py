from ll import LinkedList, Node

def splitAlternate(l):
    l1 = LinkedList()
    l1.head = Node('*')
    tail = l1.head
    node = l.head
    while node and node.next:
        next = node.next
        tail.next = next
        tail = tail.next
        node.next = next.next
        tail.next = None
        node = node.next
    l1.head = l1.head.next
    return l1

a = LinkedList()
for i in range(2):
    a.append(i)
a.print()
l = splitAlternate(a)
a.print()
l.print()
