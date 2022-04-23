from tree import Node

'''
Given a binary tree, find out if the tree can be folded or not.
A tree can be folded if left and right subtrees of the tree are structure wise mirror image of each other. 
An empty tree is considered as foldable. 

Consider the below trees:
(a) and (b) can be folded.
(c) and (d) cannot be folded.

(a)
       10
     /    \
    7      15
     \    /
      9  11

(b)
        10
       /  \
      7    15
     /      \
    9       11

(c)
        10
       /  \
      7   15
     /    /
    5   11

(d)

         10
       /   \
      7     15
    /  \    /
   9   10  12
'''


def isFoldableUtil(a, b):
    if a is None and b is None:
        return True
    if a is None or b is None:
        return False
    return isFoldableUtil(a.left, b.right) and isFoldableUtil(a.right, b.left)

def isFoldable(root):
    if root is None:
        return True
    return isFoldableUtil(root.left, root.right)
    


root = Node(10)
root.left = Node(7)
root.right = Node(15)
root.left.right = Node(9)
root.right.left = Node(11)

print(isFoldable(root))
