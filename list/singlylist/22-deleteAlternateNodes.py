from ll import LinkedList, Node

def deleteAlternate(node):
    while node and node.next:
        next = node.next
        node.next = next.next
        next.next = None
        node = node.next

a = LinkedList()
for i in range(2):
    a.append(i)
a.print()
deleteAlternate(a.head)
a.print()