from ll import LinkedList, Node

def moveAllOccurencesToEnd(l, x):
    if l.head is None:
        return
    lastNode = l.head
    while lastNode.next:
        lastNode = lastNode.next
    prev, current = None, l.head
    firstOccNode = None
    while current and current != firstOccNode:
        next = current.next
        if current.data == x and next:
            if firstOccNode == None:
                firstOccNode = current
            if current == l.head:
                l.head = next
                current.next = None
                lastNode.next = current
                lastNode = lastNode.next
            else:
                prev.next = next
                current.next = None
                lastNode.next = current
                lastNode = lastNode.next
        prev, current = current, next

a = LinkedList()
a.append(6)   
a.append(6)
a.append(7)          
a.append(6)
a.append(3)
a.append(10)        
a.print()
moveAllOccurencesToEnd(a, 10)
a.print()         