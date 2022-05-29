from collections import defaultdict, deque
from typing import Counter
from bst import Node, insert, search, preorder

# 1, 6, 7, 9
# 12
'''
            8
          /   \
        3      15 
       / \    /  \
      1   7  10   17
               \
                14

            11
          /    \
         9      12
        /         \
       6           16
'''

def treeToSortedList(root, tail):
    if root:
        treeToSortedList(root.left, tail)
        tail[0].right = root
        root.left = None
        tail[0] = root
        treeToSortedList(root.right, tail)

def merge(a, b):
    head = tail = Node('*')
    while a and b:
        if a.data <= b.data:
            tail.right = a
            tail = tail.right
            a = a.right
        else:
            tail.right = b
            tail = tail.right
            b = b.right
    if a:
        tail.right = a
    if b:
        tail.right = b
    return head.right

def findMiddle(root):
    fast, slow, prevSlow = root, root, None
    while fast and fast.right:
        fast = fast.right.right
        prevSlow, slow = slow, slow.right
    return prevSlow, slow

def listToBalancedBST(head):
    if head is None:
        return None
    if head.right is None:
        return head
    (prevMid, mid) = findMiddle(head)
    nextToMid = mid.right
    mid.right = None
    prevMid.right = None
    mid.left = listToBalancedBST(head)
    mid.right = listToBalancedBST(nextToMid)
    return mid

def mergeTrees(a, b):
    head = tail = Node('*')
    treeToSortedList(a, [tail])
    head1 = head.right
    treeToSortedList(b, [tail])
    head2 = head.right
    head = merge(head1, head2)
    return listToBalancedBST(head)

'''
            8
          /   \
        3      15 
       / \    /  \
      1   7  10   17
               \
                14

            11
          /    \
         9      12
        /         \
       6           16
'''
# 1 3 6 7 8 9 10 11 12 14 15
root1 = Node(8)
insert(root1, 3)
insert(root1, 15)
insert(root1, 10)
insert(root1, 17)
insert(root1, 14)
insert(root1, 1)
insert(root1, 7)

root2 = Node(11)
insert(root2, 9)
insert(root2, 6)
insert(root2, 12)
insert(root2, 16)

preorder(mergeTrees(root1, root2))
print()