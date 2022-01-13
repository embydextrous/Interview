from ll import LinkedList, Node

def detectLoop(node):
    fast, slow = node, node
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return True
    return False

a = LinkedList()
for i in range(5):
    a.append(i)
a.print()
print(detectLoop(a.head))
a.head.next.next.next.next.next = a.head.next.next
print(detectLoop(a.head))