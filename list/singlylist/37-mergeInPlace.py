from ll import LinkedList, Node
from random import randint

def merge(a, s):
    head = tail = Node('*')
    b = s.head
    while a and b:
        nextA, nextB = a.next, b.next
        tail.next = a
        tail = tail.next
        tail.next = b
        tail = tail.next
        a, b = nextA, nextB
    if a:
        tail.next = a
    else:
        tail.next = None
    s.head = b

a = LinkedList()
b = LinkedList()
for i in range(5):
    a.append(randint(1, 20))
for i in range(5):
    b.append(randint(1, 20))
a.print()
b.print()
merge(a.head, b)
a.print()
b.print()
