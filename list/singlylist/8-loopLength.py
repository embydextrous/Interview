from ll import LinkedList, Node

def loopLength(node):
    fast, slow = node, node
    loopNode = None
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            loopNode = slow
            break
    if loopNode is None:
        return 0
    a = loopNode.next
    length = 1
    while a is not loopNode:
        a = a.next
        length += 1
    return length

a = LinkedList()
for i in range(8):
    a.append(i)
a.print()

a.head.next.next.next.next.next.next.next.next = a.head.next.next.next

print(loopLength(a.head))
