from ll import LinkedList, Node

def getNth(node, n):
    while node:
        if n == 1:
            break
        n -= 1
        node = node.next
    return node

def getNthFromEnd(node, n):
    a, b = node, node
    while a:
        if n == 1:
            break
        n -= 1
        a = a.next
    if a is None:
        return None
    while a.next:
        a, b = a.next, b.next
    return b

a = LinkedList()
for i in range(5):
    a.append(i)
a.print()

for i in range(8):
    node = getNthFromEnd(a.head, i)
    if node:
        print(node.data)
    else:
        print(node)