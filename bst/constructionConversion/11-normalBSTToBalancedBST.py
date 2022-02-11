from bst import Node, preorder

def findMiddle(root):
    fast, slow, prevSlow = root, root, None
    while fast and fast.right:
        fast = fast.right.right
        slow, prevSlow = slow.right, slow
    return (prevSlow, slow)

def sortedListToBst(head):
    if head is None:
        return None
    if head.right is None:
        return head
    prevMid, mid = findMiddle(head)
    prevMid.right = None
    nextToMid = mid.right
    mid.right = None
    mid.left = sortedListToBst(head)
    mid.right = sortedListToBst(nextToMid)
    return mid

def inorder(root, tail):
    if root:
        inorder(root.left, tail)
        tail[0].right = root
        root.left = None
        tail[0] = root
        inorder(root.right, tail)

# Simple, take inorder traversal and use Q4
def bstToBalancedBst(root):
    if root is None:
        return None
    dummy = Node('*')
    head = tail = [dummy]
    tail = [dummy]
    inorder(root, tail)
    next = head[0].right
    head[0].right = None
    return sortedListToBst(next)

'''
        10
        /
       8
      /
     7
    /
   6
  / 
 5

            7
          /   \
         6    10
        /     /
       5     8       
'''

root = Node(10)
root.left = Node(8)
root.left.left = Node(7)
root.left.left.left = Node(6)
root.left.left.left.left = Node(5)

preorder(bstToBalancedBst(root))
print()