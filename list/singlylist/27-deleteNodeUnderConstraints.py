from ll import LinkedList, Node

# https://www.geeksforgeeks.org/delete-a-given-node-in-linked-list-under-given-constraints/

def delete(firstNode, nodeToBeDeleted):
    if firstNode == nodeToBeDeleted:
        firstNode.data = firstNode.next.data
        firstNode.next = firstNode.next.next
    else:
        prev, current = None, firstNode
        while current is not nodeToBeDeleted:
            prev, current = current, current.next
        prev.next = current.next

a = LinkedList()
for i in range(3):
    a.append(i)
a.print()
delete(a.head, a.head.next.next)
a.print()