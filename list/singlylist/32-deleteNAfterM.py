from ll import LinkedList, Node

# n >= 1, m >= 1
def deleteNAfterM(node, m, n):
    while node:
        i, j = m, n
        while node and i > 1:
            node = node.next
            i -= 1
        while node and node.next and j > 0:
            node.next = node.next.next
            j -= 1
        if node:
            node = node.next

a = LinkedList()
for i in range(10):
    a.append(i)
a.print()
deleteNAfterM(a.head, 1, 2)
a.print()
