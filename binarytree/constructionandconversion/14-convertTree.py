# https://www.geeksforgeeks.org/convert-an-arbitrary-binary-tree-to-a-tree-that-holds-children-sum-property/

from tree import Node, inorder

'''
Given an arbitrary binary tree, convert it to a binary tree that holds Children Sum Property. 
You can only increment data values in any node (You cannot change the structure of the tree and 
cannot decrement the value of any node). 
For example, the below tree doesn't hold the children sum property, convert it to a tree that holds
the property.

              50
           /     \     
          /       \
         7         2
        / \       / \
       /   \     /   \
      3     5   1     30
'''

def convert(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return root.data
    left = convert(root.left)
    right = convert(root.right)
    if left + right >= root.data:
        root.data = left + right
    else:
        increment(root, root.data - left - right)
    return root.data

def increment(root, diff):
    if root.left:
        root.left.data += diff
        increment(root.left, diff)
    elif root.right:
        root.right.data += diff
        increment(root.right, diff)

root = Node(50)
root.left = Node(7)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(5)
root.right.left = Node(1)
root.right.right = Node(30)

convert(root)
inorder(root)
print()



    
