from ll import LinkedList, Node

def insertMiddle(a, node):
    if a.head is None:
        a.head = node
        return
    fast, slow, prevSlow, c = a.head, a.head, None, 0
    while fast and fast.next:
        fast = fast.next.next
        prevSlow, slow = slow, slow.next
        c += 2
    if fast:
        c += 1
    if c % 2 == 0:
        node.next = prevSlow.next
        prevSlow.next = node
    else:
        node.next = slow.next
        slow.next = node

a = LinkedList()
a.append(1)
a.append(2)
a.append(3)
a.append(4)
insertMiddle(a, Node('*'))
a.print()