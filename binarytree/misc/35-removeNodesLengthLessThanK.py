# https://www.geeksforgeeks.org/remove-nodes-root-leaf-paths-length-k/
from tree import Node, inorder

'''
Given a Binary Tree and a number k, remove all nodes that lie only on root to leaf path(s) of length smaller 
than k. If a node X lies on multiple root-to-leaf paths and if any of the paths has path length >= k, 
then X is not deleted from Binary Tree. In other words a node is deleted if all paths going through it 
have lengths smaller than k.
Consider the following example Binary Tree 
 

               1
           /      \
         2          3
      /     \         \
    4         5        6
  /                   /
 7                   8 
Input: Root of above Binary Tree
       k = 4

Output: The tree should be changed to following  
           1
        /     \
      2          3
     /             \
   4                 6
 /                  /
7                  8
'''

def remove(root, pathlen, k):
    if root is None:
        return None
    pathlen += 1
    root.left = remove(root.left, pathlen, k)
    root.right = remove(root.right, pathlen, k)
    if root.left is None and root.right is None and pathlen < k:
        return None
    return root

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)
root.left.left.left = Node(7)
root.right.right.left = Node(8)

root = remove(root, 0, 5)
inorder(root)
print()