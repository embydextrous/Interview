from ll import LinkedList, Node

def countRotations(node):
    c = 0
    while node and node.next:
        c += 1
        if node.data > node.next.data:
            break
        node = node.next
    if node.next is None:
        return 0
    return c

l = LinkedList()
l.append(4)
l.append(5)
l.append(6)
l.append(1)
l.append(2)
l.append(3)


l.print()
print(countRotations(l.head))