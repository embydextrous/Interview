from dll import DoublyLinkedList, Node

# https://www.geeksforgeeks.org/non-repeating-element/
def firstNonRepeatingElement(s):
    d = {}
    dll = DoublyLinkedList()
    tail = None
    for c in s:
        if c in d:
            if d[c]:
                if d[c].next is None:
                    tail = d[c].prev
                dll.delete(d[c])
                d[c] = None
        else:
            newNode = Node(c)
            if tail == None:
                dll.head = newNode
                tail = newNode
            else:
                tail.next = newNode
                newNode.prev = tail
                tail = newNode
            d[c] = newNode
        dll.print()
    if dll.head:
        return dll.head.data
    return None

s = "geekforgeekandgeeksandquizfor"
print(firstNonRepeatingElement(s))
