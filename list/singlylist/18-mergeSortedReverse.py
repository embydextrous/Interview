from ll import LinkedList, Node

def mergeSort(a, b):
    result = LinkedList()
    while a and b:
        if a.data <= b.data:
            nextA = a.next
            a.next = result.head
            result.head = a
            a = nextA
        else:
            nextB = b.next
            b.next = result.head
            result.head = b
            b = nextB
    while a:
        nextA = a.next
        a.next = result.head
        result.head = a
        a = nextA
    while b:
        nextB = b.next
        b.next = result.head
        result.head = b
        b = nextB
    return result

a = LinkedList()
a.append(1)
a.append(4)
a.append(6)
a.append(9)
a.print()


b = LinkedList()
b.append(2)
b.append(3)
b.append(8)
b.append(10)
b.print()

mergeSort(a.head, b.head).print()