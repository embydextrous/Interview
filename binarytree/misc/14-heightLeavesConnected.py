from tree import Node

# https://www.geeksforgeeks.org/find-height-of-a-special-binary-tree-whose-leaf-nodes-are-connected/

def height(root):
    if root is None:
        return 0
    if root.left and root.left.right == root:
        return 1
    if root.right and root.right.left == root:
        return 1
    lHeight = height(root.left)
    rHeight = height(root.right)
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
root.left.left.left = Node(6)
root.left.left.left.right = root.left.right
root.left.right.left = root.left.left.left
root.left.right.right = root.right
root.right.left = root.left.right

print(height(root))