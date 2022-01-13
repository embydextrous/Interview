from ll import LinkedList, Node

def deleteNAfterM(l, n, m):
    if m == 0:
        node = l.head
        while l.head:
            l.head = l.head.next
            n -= 1
            if n == 0:
                break
    else:
        node = l.head
        while node:
            m -= 1
            if m == 0:
                break
            node = node.next
        while node and node.next:
            node.next = node.next.next
            n -= 1
            if n == 0:
                break


a = LinkedList()
for i in range(10):
    a.append(i)
a.print()
deleteNAfterM(a, 3, 7)
a.print()
