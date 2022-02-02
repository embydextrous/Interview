# https://www.geeksforgeeks.org/merge-two-binary-trees-node-sum/

from tree import Node, inorder

'''
Given two binary trees. We need to merge them into a new binary tree. 
The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. 
Otherwise, the non-null node will be used as the node of new tree.

Example:  

Input: 
     Tree 1            Tree 2                  
       2                 3                             
      / \               / \                            
     1   4             6   1                        
    /                   \   \                      
   5                     2   7                  

Output: Merged tree:
         5
        / \
       7   5
      / \   \ 
     5   2   7
'''

def merge(a, b):
    if a is None and b is None:
        return None
    if a is None:
        return b
    if b is None:
        return a
    a.data = a.data + b.data
    a.left = merge(a.left, b.left)
    a.right = merge(a.right, b.right)
    return a

a = Node(2)
a.left = Node(1)
a.right = Node(4)
a.left.left = Node(5)

b = Node(3)
b.left = Node(6)
b.right = Node(1)
b.left.right = Node(2)
b.right.right = Node(7)

inorder(merge(a, b))