from dll import DoublyLinkedList

def isPalindrome(node):
    if node is None or node.next is None:
        return True
    first, last = node, node.next
    while last and last.next:
        last = last.next
    while True:
        if first.data != last.data:
            return False
        first = first.next
        last = last.prev
        if first == last or first.prev == last:
            break
    return True

a = DoublyLinkedList()
a.append(4)
a.append(2)
a.append(1)
a.append(2)
a.append(0)
print(isPalindrome(a.head))