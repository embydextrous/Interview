from ll import LinkedList, Node
import heapq

def mergeKSortedLists(lists):
    h = []
    for list in lists:
        if list is not None:
            h.append(HeapNode(list))
    if len(h) == 0:
        return None
    if len(h) == 1:
        return h[0].node
    heapq.heapify(h)
    head = tail = Node('*')
    while len(h) > 1:
        heapNode = h[0]
        tail.next = heapNode.node
        tail = tail.next
        if heapNode.node.next:
            heapq.heapreplace(h, HeapNode(heapNode.node.next))
        else:
            heapq.heappop(h)
        heapNode.node.next = None
    if len(h) == 1:
        tail.next = h[0].node
    return head.next

class HeapNode:
    def __init__(self, node):
        self.node = node

    def __le__(self, other):
        return self.node.data <= other.node.data
 
a = LinkedList()
b = LinkedList()
c = LinkedList()

a.append(1)
a.append(4)
a.append(7)
a.append(12)
b.append(10)
b.append(11)
c.append(2)
c.append(7)
c.append(9)
c.append(14)
a.print()
b.print()
c.print()
l = LinkedList()
l.head = mergeKSortedLists([a.head, b.head, c.head])
l.print()