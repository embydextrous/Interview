from dll import DoublyLinkedList, Node

def sortedInsert(l, data):
    newNode = Node(data)
    if l.head is None:
        l.head = newNode
        return
    if data <= l.head.data:
        newNode.next = l.head
        l.head.prev = newNode
        l.head = newNode
        return
    current = l.head
    while current.next:
        if current.next.data >= data:
            break
        current = current.next
    newNode.next, newNode.prev = current.next, current
    current.next = newNode
    if newNode.next:
        newNode.next.prev = newNode

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

