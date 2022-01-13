from cll import CircularLinkedList, Node

def insertSorted(cll, data):
    newNode = Node(data)
    if cll.head is None:
        cll.head = newNode
        cll.head.next = newNode
    elif data <= cll.head.data:
        lastNode = cll.head
        while lastNode.next != cll.head:
            lastNode = lastNode.next
        newNode.next = cll.head
        lastNode.next = newNode
        cll.head = newNode
    else:
        prevNode = cll.head
        while prevNode.next != cll.head and prevNode.next.data < data:
            prevNode = prevNode.next
        newNode.next = prevNode.next
        prevNode.next = newNode


a = CircularLinkedList()
a.append(2)
a.append(5)
a.append(8)
a.print()
insertSorted(a, 1)
a.print()
insertSorted(a, 3)
a.print()
insertSorted(a, 5)
a.print()
insertSorted(a, 6)
a.print()
insertSorted(a, 10)
a.print()

