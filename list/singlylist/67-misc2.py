from ll import LinkedList, Node

# https://www.geeksforgeeks.org/modify-contents-linked-list/

def findMiddle(node):
    fast, slow = node, node
    while fast.next and fast.next.next:
        fast, slow = fast.next.next, slow.next
    return slow

def reverse(node):
    prev, current = None, node
    while current:
        next = current.next
        current.next = prev
        prev, current = current, next
    return prev

def modify(node):
    if node is None or node.next is None:
        return
    midNode = findMiddle(node)
    nextToMiddle = midNode.next
    midNode.next = None
    nextToMidRev = reverse(nextToMiddle)
    a, b = node, nextToMidRev
    while b:
        a.data = a.data - b.data
        a, b = a.next, b.next
    midNode.next = reverse(nextToMidRev)

a = LinkedList()
a.append(2)
a.append(9)
a.append(8)
a.append(12)
a.append(7)
a.append(10)
a.print()
modify(a.head)
a.print()