from ll import LinkedList, Node

def evenOddTogether(node):
    if node is None or node.next is None:
        return
    o, e, fe = node, node.next, node.next
    c = node.next.next
    addToOdd = True
    while c:
        if addToOdd:
            o.next = c
            o = o.next
        else:
            e.next = c
            e = e.next
        addToOdd = not addToOdd
        c = c.next
    e.next = None
    o.next = fe

a = LinkedList()
for i in range(5):
    a.append(i)
a.print()
evenOddTogether(a.head)
a.print()
