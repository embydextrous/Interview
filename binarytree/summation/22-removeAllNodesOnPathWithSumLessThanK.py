# https://www.geeksforgeeks.org/remove-all-nodes-which-lie-on-a-path-having-sum-less-than-k/
from tree import inorder, Node

'''
Given a binary tree, a complete path is defined as a path from root to a leaf. 
The sum of all nodes on that path is defined as the sum of that path. 
Given a number K, you have to remove (prune the tree) all nodes which don't lie in any path with sum>=k. 

Note: A node can be part of multiple paths. So we have to delete it only in case when all paths from it 
have sum less than K.

Consider the following Binary Tree
          1 
      /      \
     2        3
   /   \     /  \
  4     5   6    7
 / \    /       /
8   9  12      10
   / \           \
  13  14         11
      / 
     15 

For input k = 20, the tree should be changed to following
(Nodes with values 6 and 8 are deleted)
          1 
      /      \
     2        3
   /   \        \
  4     5        7
   \    /       /
    9  12      10
   / \           \
  13  14         11
      / 
     15 

For input k = 45, the tree should be changed to following.
      1 
    / 
   2   
  / 
 4  
  \   
   9    
    \   
     14 
     /
    15 
'''
def prune(root, sum):
    if root is None:
        return None
    root.left = prune(root.left, sum - root.data)
    root.right = prune(root.right, sum - root.data)
    if root.left is None and root.right is None:
        if sum > root.data:
            return None
    return root

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.left.left = Node(8)
root.left.left.right = Node(9)
root.left.right.left = Node(12)
root.right.right.left = Node(10)
root.left.left.right.left = Node(13)
root.left.left.right.right = Node(14)
root.right.right.left.right = Node(11)
root.left.left.right.right.left = Node(15)

prune(root, 45)
inorder(root)
print()