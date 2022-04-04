from ll import LinkedList, Node

def reverse(node):
    prev, current = None, node
    while current:
        next = current.next
        current.next = prev
        prev, current = current, next
    return prev

def checkPalindrome(node):
    if node is None or node.next is None:
        return True
    fast, slow, prevSlow = node, node, None
    while fast and fast.next:
        fast = fast.next.next
        prevSlow, slow = slow, slow.next
    first, second = node, reverse(slow)
    secondCopy = second
    isPalindrome = True
    while first and second:
        if first.data != second.data:
            isPalindrome = False
            break
        first, second = first.next, second.next
    prevSlow.next = reverse(secondCopy)
    return isPalindrome

a = LinkedList()
a.append(1)
a.append(1)
a.insertAfter(a.head, 2)
a.insertAfter(a.head, 2)
a.insertAfter(a.head, 3)
a.insertAfter(a.head.next.next.next, 3)
a.print()
print(checkPalindrome(a.head))
a.print()