from cll import CircularLinkedList
#from ll import LinkedList

def isCircular(node):
    if node is None:
        return True
    current = node
    while current:
        if current.next == node:
            return True
        current = current.next
    return False

#a = LinkedList()
b = CircularLinkedList()
b.print()
print(isCircular(b.head))
b.append(1)
b.print()
print(isCircular(b.head))
b.append(2)
b.print()
print(isCircular(b.head))
b.append(3)
b.print()
print(isCircular(b.head))
b.append(4)
b.print()
print(isCircular(b.head))
b.append(5)
b.print()
print(isCircular(b.head))
b.append(6)
b.print()
print(isCircular(b.head))
