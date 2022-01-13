from ll import LinkedList, Node
from random import randint

def sort(a):
    c0 = c1 = c2 = 0
    node = a
    while a:
        if a.data == 0:
            c0 += 1
        elif a.data == 1:
            c1 += 1
        elif a.data == 2:
            c2 += 1
        a = a.next
    while node:
        if c0 != 0:
            node.data = 0
            c0 -= 1
        elif c1 != 0:
            node.data = 1
            c1 -= 1
        elif c2 != 0:
            node.data = 2
            c2 -= 1
        node = node.next

a = LinkedList()
for i in range(10):
    a.append(randint(0, 100) % 3)
a.print()
sort(a.head)
a.print()