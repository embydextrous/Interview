from tree import Node

def checkBalanced(left, right):
    if left is None and right is None:
        return True
    if left is None:
        return not right.left and not right.right
    if right is None:
        return not left.right and not left.left
    return checkBalanced(left.left, left.right) and checkBalanced(right.left, right.right)

def isBalanced(root):
    if root is None:
        return True
    return checkBalanced(root.left, root.right)

'''
Constructed binary tree is
         1
       /   \
      2     3
     / \   /
    4   5 6 
    / 
   7
'''
# to store the height of tree during traversal
 
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.left.left.left = Node(7)
root.left.left.left.left = Node(8)

print(isBalanced(root))