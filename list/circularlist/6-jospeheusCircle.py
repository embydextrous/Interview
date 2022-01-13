from cll import CircularLinkedList

def getJospeheusPosition(n, k):
    cll = CircularLinkedList()
    for i in range(1, n + 1):
        cll.append(i)
    return getJosepheusPositionInternal(cll.head, k)
    

def getJosepheusPositionInternal(node, k):
    if node == node.next:
        return node.data
    else:
        n = k - 1
        prev, current = node, node.next
        while n > 0:
            n -= 1
            if n == 0:
                break
            prev, current = current, current.next
        prev.next = current.next
        return getJosepheusPositionInternal(prev.next, k)


print(getJospeheusPosition(100, 1))