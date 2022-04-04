from ll import LinkedList, Node

def pairwiseSwap(node):
    if node is None or node.next is None:
        return node
    a, b = node, node.next
    next = b.next
    b.next = a
    a.next = pairwiseSwap(next)
    return b


a = LinkedList()
for i in range(10):
    a.append(i)
a.print()
a.head = pairwiseSwap(a.head)
a.print()