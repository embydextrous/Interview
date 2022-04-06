from dll import DoublyLinkedList, Node

def sortedInsert(l, data):
    newNode = Node(data)
    if l.head is None:
        l.head = newNode
        return
    current = l.head
    while current and current.data < data:
        if current.next is None:
            break
        current = current.next
    if current.data < data:
        current.next = newNode
        newNode.prev = current
        return
    newNode.next = current
    newNode.prev = current.prev
    current.prev = newNode
    if newNode.prev:
        newNode.prev.next = newNode
    else:
        l.head = newNode

a = DoublyLinkedList()
a.append(3)
a.append(5)
a.append(8)
a.append(10)
a.append(12)
a.print()

sortedInsert(a, 1)
a.print()
sortedInsert(a, 2)
a.print()
sortedInsert(a, 4)
a.print()
sortedInsert(a, 6)
a.print()
sortedInsert(a, 7)
a.print()
sortedInsert(a, 9)
a.print()
sortedInsert(a, 11)
a.print()
sortedInsert(a, 13)
a.print()

