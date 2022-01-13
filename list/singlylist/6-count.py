from ll import LinkedList, Node

def count(node, k):
    c = 0
    while node:
        if node.data == k:
            c += 1
        node = node.next
    return c

a = LinkedList()
a.append(1)
a.append(2)
a.append(1)
a.append(3)
a.append(2)
a.append(3)
a.append(3)
a.append(3)

for i in range(5):
    print(count(a.head, i))

