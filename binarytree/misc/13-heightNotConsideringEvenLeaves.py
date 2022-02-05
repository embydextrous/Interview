from tree import Node

# https://www.geeksforgeeks.org/height-binary-tree-considering-even-level-leaves/

def height(root, level):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return level % 2
    lHeight = height(root.left, level + 1)
    rHeight = height(root.right, level + 1)
    return 1 + max(lHeight, rHeight)

'''
            1
          /   \
         2     3
       /   \
      4     5
           /
         6  
'''

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
#root.left.right.left = Node(6)

print(height(root, 0))