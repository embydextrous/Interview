from ll import LinkedList, Node

def reverse(node):
    prev = None
    while node:
        next = node.next
        node.next = prev
        prev, node = node, next
    return prev

def delete(node, m, n):
    if m == 0:
        while node and n > 0:
            next = node.next
            node.next = None
            node = next
            n -= 1
        return node
    else:
        current = node
        while current and m > 1:
            current = current.next
            m -= 1
        while current and current.next and n > 0:
            current.next = current.next.next
            n -= 1
        return node

    
a = LinkedList()
for i in range(15):
    a.append(i)
a.print()

a.head = delete(a.head, 4, 18)
a.print()