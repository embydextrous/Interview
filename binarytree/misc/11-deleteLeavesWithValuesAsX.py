from tree import Node, inorder

def deleteLeaves(root, x):
    if root is None:
        return None
    root.left = deleteLeaves(root.left, x)
    root.right = deleteLeaves(root.right, x)
    if root.left is None and root.right is None:
        if root.data == x:
            return None
    return root
    
root = Node(8)
root.left = Node(3)
root.left.left = Node(1)
root.left.right = Node(16)
root.right = Node(10)
root.right.left = Node(7)
root.right.right = Node(14)

'''
        8
      /   \
     3     10
   /   \   /  \
  1    16 7   14
'''

deleteLeaves(root, 1)
inorder(root)
print()
