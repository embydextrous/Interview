from ll import LinkedList, Node

def reverse(node):
    prev = None
    while node:
        next = node.next
        node.next = prev
        prev, node = node, next
    return prev

def deleteLast(l, key):
    l.head = reverse(l.head)
    prev, current = None, l.head
    while current:
        if current.data == key:
            break
        prev, current = current, current.next
    if current is None:
        return
    if prev:
        prev.next = current.next
    else:
        l.head = current.next
    l.head = reverse(l.head)

a = LinkedList()
a.append(1)
a.append(2)
a.append(2)
a.append(4)
a.append(3)
a.append(2)
a.append(4)
a.append(1)
a.print()
deleteLast(a, 1)
a.print()
deleteLast(a, 1)
a.print()

deleteLast(a, 2)
a.print()

deleteLast(a, 4)
a.print()




