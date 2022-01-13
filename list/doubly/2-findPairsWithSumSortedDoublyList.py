from dll import DoublyLinkedList

def findPairWithSum(node, x):
    if node is None:
        return
    l, r = node, node
    while r.next:
        r = r.next
    while l != r:
        if l.data + r.data == x:
            return (l.data, r.data)
        elif l.data + r.data < x:
            l = l.next
        else:
            r = r.prev
    return None


a = DoublyLinkedList()

for i in range(10):
    a.append(i)
a.print()

for i in range(1, 20):
    print(str(i) + " -> "+ str(findPairWithSum(a.head, i)))