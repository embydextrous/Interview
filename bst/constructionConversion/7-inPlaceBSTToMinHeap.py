from bst import Node, insert, inorder

# Also see, https://www.geeksforgeeks.org/convert-bst-min-heap/
from collections import deque

def bstToSortedList(root, tail):
    if root:
        bstToSortedList(root.left, tail)
        tail[0].right = root
        root.left = None
        tail[0] = root
        bstToSortedList(root.right, tail)

def sortedListToTree(head):
    if head is None:
        return
    q = deque([head])
    head = head.right
    while head:
        node = q.popleft()
        node.left = head
        q.append(node.left)
        head = head.right
        node.right = head
        if head:
            q.append(node.right)
            head = head.right
    while len(q) > 0:
        node = q.popleft()
        node.left, node.right = None, None
        
def bstToMinHeap(root):
    if root is None:
        return
    dummyNode = Node('*')
    tail = [dummyNode]
    bstToSortedList(root, tail)
    ret = dummyNode.right
    dummyNode.right = None   
    sortedListToTree(ret)
    return ret

root = Node(8)
insert(root, 4)
insert(root, 12)
insert(root, 2)
insert(root, 6)
insert(root, 10)
insert(root, 14)

root = bstToMinHeap(root)
inorder(root)
print()
