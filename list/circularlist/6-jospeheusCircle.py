from cll import CircularLinkedList

def getJospeheusPosition(n, k):
    cll = CircularLinkedList()
    for i in range(1, n + 1):
        cll.append(i)
    return getJosepheusPositionInternal(cll.head, k)
    
def getJosepheusPositionInternal(node, k):
    prev, current = None, node
    while current != current.next:
        n = k
        while n > 0:
            n -= 1
            prev, current = current, current.next
        prev.next = current.next
    return current.data

print(getJospeheusPosition(1000000, 1))