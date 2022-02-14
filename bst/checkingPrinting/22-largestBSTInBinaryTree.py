from bst import Node, inorder
import sys

MINI = sys.maxsize
MAXI = -MINI-1

def largestBSTUtil(root, result):
    if root is None:
        return (True, None, None)
    if root.left is None and root.right is None:
        return (True, root.data, root.data)
    left = largestBSTUtil(root.left, result)
    right = largestBSTUtil(root.right, result)
    if not left[0] or not right[0]:
        return (False, None, None)
    if root.left is None:
        if root.data < right[1]:
            result[0] = root
            return (True, root.data, right[2])
        else:
            return (False, None, None)
    if root.right is None:
        if root.data < left[2]:
            result[0] = root
            return (True, left[1], root.data)
        else:
            return (False, None, None)
    if root.data < right[1] and root.data > left[2]:
        result[0] = root
        return (True, left[1], right[2])
    else:
        return (False, None, None)

def largestBST(root):
    result = [None]
    largestBSTUtil(root, result)
    return result[0]

'''
       50
     /    \
  30       60
 /  \     /  \ 
5   20   45    70
              /  \
            65    80
'''
root = Node(50)
root.left = Node(30)
root.right = Node(60)
root.left.left = Node(5)
root.left.right = Node(20)
root.right.left = Node(45)
root.right.right = Node(70)
root.right.right.left = Node(65)
root.right.right.right = Node(80)

inorder(largestBST(root))
print()