from ll import LinkedList, Node

def intersection(a, b):
    head = tail = Node('*')
    while a and b:
        if a.data == b.data:
            tail.next = a
            tail = tail.next
            a = a.next
            b = b.next
        elif a.data < b.data:
            a = a.next
        else:
            b = b.next
    tail.next = None
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