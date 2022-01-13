from ll import LinkedList, Node

def breakLoop(node):
    fast, slow = node, node
    loopNode = None
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            loopNode = slow
            break
    if loopNode == None:
        return
    while loopNode.next != node.next:
        loopNode, node = loopNode.next, node.next
    loopNode.next = None

a = LinkedList()
for i in range(6):
    a.append(i)
a.head.next.next.next.next.next.next = a.head.next.next.next
breakLoop(a.head)
a.print()