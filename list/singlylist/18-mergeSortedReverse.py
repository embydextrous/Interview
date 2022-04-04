from ll import LinkedList, Node

def mergeSort(a, b):
    if a is None and b is None:
        return None
    head = Node('*')
    firstNode = None
    while a and b:
        if a.data <= b.data:
            next = a.next
            a.next = head
            head = a
            a = next
        else:
            next = b.next
            b.next = head
            head = b
            b = next
        if not firstNode:
            firstNode = head
    while a:
        next = a.next
        a.next = head
        head = a
        a = next
        if not firstNode:
            firstNode = head
    while b:
        next = b.next
        b.next = head
        head = b
        b = next
        if not firstNode:
            firstNode = head
    firstNode.next = None
    return head


a = LinkedList()
a.append(1)
a.append(4)
a.append(6)
a.append(9)
a.print()


b = LinkedList()
b.append(2)
b.append(3)
b.append(8)
b.append(10)
b.print()

c = LinkedList()
c.head = mergeSort(a.head, b.head)
c.print()