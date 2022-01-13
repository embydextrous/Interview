from cll import CircularLinkedList
#from ll import LinkedList

def size(node):
    if node is None:
        return 0
    c = 0
    current = node
    while current:
        c += 1
        if current.next == node:
            break
        current = current.next
    return c

#a = LinkedList()
b = CircularLinkedList()
b.print()
print(size(b.head))
b.append(1)
b.print()
print(size(b.head))
b.append(2)
b.print()
print(size(b.head))
b.append(3)
b.print()
print(size(b.head))
b.append(4)
b.print()
print(size(b.head))
b.append(5)
b.print()
print(size(b.head))
b.append(6)
b.print()
print(size(b.head))
