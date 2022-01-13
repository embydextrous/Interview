from ll import LinkedList, Node

def reverse(node):
    prev = None
    while node:
        next = node.next
        node.next = prev
        prev, node = node, next
    return prev

def sort(l):
    node = l.head
    posHead = pos = Node('*')
    negHead = neg = Node('*')
    current = node
    while current:
        next = current.next
        if current.data >= 0:
            pos.next = current
            pos = pos.next
        else:
            neg.next = current
            neg = neg.next
        current.next = None
        current = next
    posHead = posHead.next
    negHead = negHead.next
    if negHead is None:
        return posHead
    if posHead is None:
        return negHead
    l.head = reverse(negHead)
    negHead.next = posHead

llist = LinkedList()
llist.push(-5)
llist.push(5)
llist.push(-4)
llist.push(3)
llist.push(-2)
llist.push(1)
llist.push(0)
llist.print()
sort(llist)
llist.print()
    
