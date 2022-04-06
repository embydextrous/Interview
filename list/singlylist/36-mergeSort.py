from ll import LinkedList, Node
from random import randint

def findMiddle(node):
    fast, slow = node, node
    while fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next
    return slow

def sortedMerge(a, b):
    head = tail = Node('*')
    while a and b:
        if a.data <= b.data:
            tail.next = a
            tail = tail.next
            a = a.next
        else:
            tail.next = b
            tail = tail.next
            b = b.next
    if a:
        tail.next = a
    if b: 
        tail.next = b
    return head.next
    
def mergeSortInternal(node):
    if node is None or node.next is None:
        return node
    midNode = findMiddle(node)
    nextMid = midNode.next
    midNode.next = None
    left = mergeSortInternal(node)
    right = mergeSortInternal(nextMid)
    return sortedMerge(left, right)    

def mergeSort(l):
    l.head = mergeSortInternal(l.head)

l = LinkedList()
for i in range(10):
    l.append(randint(1, 20))
l.print()
mergeSort(l)
l.print()