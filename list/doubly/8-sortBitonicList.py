from dll import DoublyLinkedList, Node

def reverse(node):
    while True:
        node.next, node.prev = node.prev, node.next
        if node.prev is None:
            break
        node = node.prev
    return node

def sortedMerge(a, b):
    head = tail = Node('*')
    while a and b:
        if a.data <= b.data:
            tail.next = a
            a.prev = tail
            tail = tail.next
            a = a.next
        else:
            tail.next = b
            b.prev = tail
            tail = tail.next
            b = b.next
    if a:
        tail.next = a
        a.prev = tail
    if b:
        tail.next = b
        b.prev = tail
    head.next.prev = None
    return head.next


def sortBitonicList(l):
    current = l.head
    while current and current.next:
        if current.data > current.next.data:
            break
        current = current.next
    if current is None or current.next is None:
        return
    next = current.next
    current.next, next.prev = None, None
    a = reverse(next)
    l.head, l.tail = sortedMerge(l.head, a), current

a = DoublyLinkedList()
a.append(2)
a.append(3)
a.append(5)
a.append(8)
a.append(6)
a.append(4)
a.append(1)
a.print()
sortBitonicList(a)
a.print()
a.printReverse()
