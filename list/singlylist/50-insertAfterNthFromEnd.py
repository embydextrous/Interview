from ll import LinkedList, Node

def insert(l, newNode, k):
    a, b = l.head, l.head
    while a and k > 0:
        k -= 1
        a = a.next
    if a is None:
        newNode.next = l.head
        l.head = newNode
    else:
        while a:
            a, b = a.next, b.next
        newNode.next = b.next
        b.next = newNode

a = LinkedList()
for i in range(10):
    a.append(i)
a.print()

insert(a, Node(12), 4)
a.print()
