from dll import DoublyLinkedList

def rotate(l, k):
    current = l.head
    while current and k > 0:
        k -= 1
        current = current.next
    if current is None or current is l.head:
        return
    lastNode = current
    while lastNode.next:
        lastNode = lastNode.next
    current.prev.next, current.prev = None, None
    lastNode.next = l.head
    l.head.prev = lastNode
    l.head = current

a = DoublyLinkedList()
for i in range(8):
    a.append(i)
a.print()
rotate(a, 8)
a.print()