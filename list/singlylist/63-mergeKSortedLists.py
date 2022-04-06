import heapq
from ll import LinkedList, Node

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

    def __lt__(self, other):
        return self.node.data < other.node.data

a = LinkedList()
b = LinkedList()
c = LinkedList()

b.append(1)
b.append(1)
c.append(1)
c.append(1)
c.append(1)
c.append(1)
c.append(1)

a.print()
b.print()
c.print()
result = LinkedList()
result.head = mergeKSortedLists([a.head, b.head, c.head])
result.print()