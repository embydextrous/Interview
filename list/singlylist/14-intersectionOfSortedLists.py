from ll import LinkedList, Node

def intersection(a, b):
    head = tail = Node('*')
    while a and b:
        if a.data == b.data:
            tail.next = Node(a.data)
            tail = tail.next
            a, b = a.next, b.next
        elif a.data > b.data:
            b = b.next
        else:
            a = a.next
    result = LinkedList()
    result.head = head.next
    return result

a = LinkedList()
for i in range(8):
    a.append(i)
a.print()
b = LinkedList()
for i in range(5):
    b.append(i * 2)
b.print()

intersection(a.head, b.head).print()