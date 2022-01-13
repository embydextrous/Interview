from ll import LinkedList, Node

def reverseAlternateKNodes(node, k, shallReverse):
    prev, current, n = None, node, k
    while current and n > 0:
        next = current.next
        if shallReverse:
            current.next = prev
        prev, current = current, next
        n -= 1
    if next:
        if shallReverse:
            node.next = reverseAlternateKNodes(next, k, False)
        else:
            prev.next = reverseAlternateKNodes(next, k, True)
    if shallReverse:
        return prev
    else:
        return node

a = LinkedList()
for i in range(8):
    a.append(i)
a.print()

a.head = reverseAlternateKNodes(a.head, 3, True)
a.print()
