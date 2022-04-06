from ll import LinkedList, Node
from random import randint

# https://www.geeksforgeeks.org/select-a-random-node-from-a-singly-linked-list/
def selectRandomNode(node):
    result = node
    current = node.next
    count = 2
    while current:
        if randint(0, count - 1) == 0:
            result = current
        count += 1
        current = current.next
    return result

l = LinkedList()
for i in range(10):
    l.append(i)
for i in range(10):
    print(selectRandomNode(l.head).data)
