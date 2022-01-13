from ll import LinkedList, Node

def areIdentical(a, b):
    if a is None and b is None:
        return True
    if a is None or b is None:
        return False
    return a.data == b.data and areIdentical(a.next, b.next)

a = LinkedList()
for i in range(5):
    a.append(i)
a.print()
b = LinkedList()
for i in range(6):
    b.append(i)
b.print()
print(areIdentical(a.head, a.head))
print(areIdentical(a.head, b.head))