from ll import LinkedList, Node
from random import randint

def pointArbitaryToNextHigherValue(a):
    if a.head is None or a.head.next is None:
        return
    current = a.head.next
    s = [a.head]
    while current:
        while current and len(s) > 0 and s[-1].data < current.data:
            s.pop().random = current
        s.append(current)
        current = current.next

a = LinkedList()
for i in range(6):
    a.append(randint(1, 50))
a.print()
pointArbitaryToNextHigherValue(a)
a.print()
current = a.head
while current:
    print(current.data, current.random.data if current.random else None)
    current = current.next

pointArbitaryToNextHigherValue(a)
a.print()
current = a.head
while current:
    print(current.data, current.random.data if current.random else None)
    current = current.next

