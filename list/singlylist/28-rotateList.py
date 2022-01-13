from ll import LinkedList, Node

def size(node):
    s = 0
    while node:
        s += 1
        node = node.next
    return s

def rotate(l, k):
    if l.head is None or l.head.next is None: 
        return
    k = k % size(l.head)
    if k == 0:
        return
    lastNode = l.head
    kthNode = l.head
    while lastNode.next:
        lastNode = lastNode.next
        k -= 1
        if k > 0:
            kthNode = kthNode.next
    lastNode.next = l.head
    l.head = kthNode.next        
    kthNode.next = None

a = LinkedList()
for i in range(10):
    a.append(i)
a.print()
rotate(a, 9)
a.print()
    
    
