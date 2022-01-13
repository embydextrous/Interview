from ll import LinkedList, Node

def reverseInGroup(node, k):
    prev, current = None, node
    n = k
    while current and n > 0:
        next = current.next
        current.next = prev
        prev, current = current, next
        n -= 1
    if next:
        node.next = reverseInGroup(next, k)
    return prev

a = LinkedList()
for i in range(8):
    a.append(i)
a.print()
a.head = reverseInGroup(a.head, 3)
a.print()