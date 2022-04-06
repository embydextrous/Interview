# https://www.geeksforgeeks.org/length-longest-palindrome-list-linked-list-using-o1-extra-space/

from ll import LinkedList, Node

def countCommon(a, b):
    c = 0
    while a and b:
        if a.data == b.data:
            c += 1
        else:
            break
        a, b = a.next, b.next
    return c

def longestPalindromicList(node):
    prev, current = None, node
    result = 0
    while current:
        next = current.next
        current.next = prev
        result = max(result, 2 * countCommon(prev, next) + 1)
        result = max(result, 2 * countCommon(current, next))
        prev, current = current, next
    # can reverse back original list here
    return result

a = LinkedList()
a.append(2)
a.append(3)
a.append(7)
a.append(3)
a.append(2)
a.append(12)
a.append(24)
a.print()
print(longestPalindromicList(a.head))

