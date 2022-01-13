from ll import LinkedList, Node

def removeKthNode(l, k):
    prev, node = None, l.head
    n = k
    while node:
        next = node.next
        k -= 1
        if k == 0:
            if prev:
                prev.next = next
            else:
                l.head = next
            node = next
            k = n
        else:
            prev, node = node, next


a = LinkedList()
for i in range(10):
    a.append(i)
a.print()
removeKthNode(a, 8)
a.print()
