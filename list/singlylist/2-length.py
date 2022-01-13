from ll import LinkedList, Node

def findLength(node):
    size = 0
    while node:
        node = node.next
        size += 1
    return size

a = LinkedList()
for i in range(10):
    a.append(i)
print(findLength(a.head)) 