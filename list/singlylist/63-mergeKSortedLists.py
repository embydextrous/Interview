from heap import buildMinHeap, minHeapify, popMinHeap, replaceMinHeap
from ll import LinkedList, Node

'''
Merge K Sorted Lists Algorithm

1. Build a minHeap of size K from first nodes
2. Pop an element and add it to result List
'''

def mergeKSortedLists(listArr):
    minHeap = []
    for node in listArr:
        if node:
            minHeap.append(node.data)
    buildMinHeap(minHeap)
    head = tail = Node('*')
    while len(minHeap) > 0:
        x = minHeap[0]
        for i in range(len(listArr)):
            if listArr[i] and listArr[i].data == x:
                tail.next = listArr[i]
                tail = tail.next
                listArr[i] = listArr[i].next
                if listArr[i]:
                    replaceMinHeap(minHeap, listArr[i].data)
                else:
                    popMinHeap(minHeap)
                tail.next = None
                break
    resultList = LinkedList()
    resultList.head = head.next
    return resultList

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
mergeKSortedLists([a.head, b.head, c.head]).print()