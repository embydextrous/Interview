from ll import LinkedList, Node

def intersectionPoint(a, b):
    lengthA = 0
    current = a
    while current:
        current = current.next
        lengthA += 1
    lengthB = 0
    current = b
    while current:
        current = current.next
        lengthB += 1
    if lengthA > lengthB:
        d = lengthA - lengthB
        while d > 0:
            a = a.next
            d -= 1
    elif lengthB > lengthA:
        d = lengthB - lengthA
        while d > 0:
            b = b.next
            d -= 1
    while a and b:
        if a == b:
            return a
        a, b = a.next, b.next
    return None




a = LinkedList()
for i in range(7):
    a.append(i)
a.print()
b = LinkedList()
b.append(9)
b.append(10)
b.append(11)
b.head.next.next.next = a.head.next.next.next.next.next
b.print

print(intersectionPoint(a.head, b.head).data)