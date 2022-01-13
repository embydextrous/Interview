from dll import DoublyLinkedList

def removeDuplicates(node):
    if node is None or node.next is None:
        return
    current = node.next
    while current:
        if current.data == current.prev.data:
            prev, next = current.prev, current.next
            current.prev, current.next = None, None
            prev.next = next
            if next:
                next.prev = prev
            current = next
        else:
            current = current.next

a = DoublyLinkedList()
a.append(4)
a.append(4)
a.append(4)
a.append(4)
a.append(6)
a.append(8)
a.append(8)
a.append(10)
a.append(12)
a.append(12)
a.print()
removeDuplicates(a.head)
a.print()