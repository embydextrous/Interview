from ll import LinkedList, Node

def findMiddle(node):
    fast, slow = node, node
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    return slow

a = LinkedList()
for i in range(7):
    a.append(i)
    a.print()
    middleNode = findMiddle(a.head)
    if middleNode:
        print(middleNode.data)
    else:
        print(None)