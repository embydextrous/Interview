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

def mergeSortInternal(node):
    if node is None or node.next is None:
        return node
    mid = findMiddle(node)
    nextMid = mid.next
    mid.next = None
    left, right = mergeSortInternal(node), mergeSortInternal(nextMid)
    return sortedMerge(left, right)

def mergeSortInternalDesc(node):
    if node is None or node.next is None:
        return node
    mid = findMiddle(node)
    nextMid = mid.next
    mid.next = None
    left, right = mergeSortInternalDesc(node), mergeSortInternalDesc(nextMid)
    return sortedMergeDesc(left, right)

def findTriplet(a, b, c, sum):
    currentA, b, c = a, mergeSortInternal(b), mergeSortInternalDesc(c)
    while currentA:
        currentB, currentC = b, c
        while currentB and currentC:
            if currentA.data + currentB.data + currentC.data == sum:
                return(currentA.data, currentB.data, currentC.data)
            elif currentA.data + currentB.data + currentC.data < sum:
                currentB = currentB.next
            else:
                currentC = currentC.next
        currentA = currentA.next
    return None

a, b, c = LinkedList(), LinkedList(), LinkedList()
a.push(20)
a.push(4)
a.push(15)
a.push(10)
a.print()

b.push(10)
b.push(9)
b.push(4)
b.push(2)
b.print()

c.push(1)
c.push(2)
c.push(4)
c.push(8)
c.print()

print(findTriplet(a.head, b.head, c.head, 35))