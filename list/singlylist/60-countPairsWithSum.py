from ll import LinkedList, Node

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

def sortedMergeDesc(a, b):
    head = tail = Node('*')
    while a and b:
        if a.data >= b.data:
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

def mergeSort(node):
    if node is None or node.next is None:
        return node
    mid = findMiddle(node)
    nextMid = mid.next
    mid.next = None
    left, right = mergeSort(node), mergeSort(nextMid)
    return sortedMerge(left, right)

def mergeSortDesc(node):
    if node is None or node.next is None:
        return node
    mid = findMiddle(node)
    nextMid = mid.next
    mid.next = None
    left, right = mergeSortDesc(node), mergeSortDesc(nextMid)
    return sortedMergeDesc(left, right)


def countPairsWithSum(a, b, x):
    a, b = mergeSort(a), mergeSortDesc(b)
    c = 0
    l = LinkedList()
    l.head = b
    l.print()
    while a and b:
        if a.data + b.data == x:
            c += 1
            a, b = a.next, b.next
        elif a.data + b.data < x:
            a = a.next
        else:
            b = b.next
    return c

a = LinkedList()
a.append(4)
a.append(3)
a.append(5)
a.append(7)
a.append(11)
a.append(2)
a.append(1)
a.print()

b = LinkedList()
b.append(2)
b.append(3)
b.append(4)
b.append(5)
b.append(6)
b.append(8)
b.append(12)
b.print()

print(countPairsWithSum(a.head, b.head, 9))

