from ll import LinkedList, Node
from random import randint, random

def reverse(node):
    prev, current = None, node
    while current:
        next = current.next
        current.next = prev
        prev, current = current, next
    return prev


def pointRandom(node):
    if node is None:
        return
    tailCopy = tail = reverse(node)
    maxi = tail
    tail = tail.next
    while tail:
        tail.random = maxi
        if tail.data > maxi.data:
            maxi = tail
        tail = tail.next
    reverse(tailCopy)


a = LinkedList()
for i in range(10):
    a.append(randint(1, 20))
a.print()
pointRandom(a.head)
a.print()
current = a.head
while current and current.next:
    print(str(current.data) + " -> " + str(current.random.data))
    current = current.next
