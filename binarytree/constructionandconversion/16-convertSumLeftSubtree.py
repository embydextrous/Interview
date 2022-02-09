# https://www.geeksforgeeks.org/change-a-binary-tree-so-that-every-node-stores-sum-of-all-nodes-in-left-subtree/
from tree import Node, inorder

def convert(root):
    if root is None:
        return 0
    left = convert(root.left)
    right = convert(root.right)
    root.data += left
    return root.data + right

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)
convert(root)
inorder(root)
print()