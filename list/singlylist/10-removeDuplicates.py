from ll import LinkedList, Node

def removeDuplicatesFromSorted(node):
    while node and node.next:
        if node.data == node.next.data:
            next = node.next
            node.next = next.next
            next.next = None
        else:
            node = node.next

def removeDuplicatesFromUnsorted(node):
    s = set()
    prev = None
    while node:
        if node.data not in s:
            s.add(node.data)
            prev, node = node, node.next
        else:
            next = node.next
            prev.next = next
            node = next


a = LinkedList()
a.append(11)
a.append(6)
a.append(2)
a.append(6)
a.append(26)
a.append(3)
a.append(4)
a.append(14)
a.append(25)
a.append(25)
a.append(16)
a.append(11)
a.append(12)
a.append(2)
a.append(12)
a.append(2)
a.append(13)
a.append(14)
a.append(4)
a.append(15)
a.append(5)
a.append(16)
a.print()
removeDuplicatesFromUnsorted(a.head)
a.print()

    