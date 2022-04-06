from ll import LinkedList, Node

def insertMiddle(a, node):
    if a.head is None:
        a.head = node
        return
    if a.head.next is None:
        a.head.next = node
        return
    fast, slow = a.head, a.head
    while fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next
    node.next = slow.next
    slow.next = node

a = LinkedList()
a.append(1)
a.append(2)
a.append(3)
a.append(4)
a.append(5)
insertMiddle(a, Node('*'))
a.print()