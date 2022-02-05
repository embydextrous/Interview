from tree import Node, inorder

def pairwiseSwapLeaves(root, leaf):
    if root is None:
        return
    if root.left is None and root.right is None:
        if leaf[0]:
            leaf[0].data, root.data = root.data, leaf[0].data
            leaf[0] = None
        else:
            leaf[0] = root
    pairwiseSwapLeaves(root.left, leaf)
    pairwiseSwapLeaves(root.right, leaf)

'''
        8
      /   \
     3     10
   /   \     \
  1    16     14
      /  \   /  \
     4    7 19   2
'''

root = Node(8)
root.left = Node(3)
root.left.left = Node(1)
root.left.right = Node(16)
root.left.right.left = Node(4)
root.left.right.right = Node(7)
root.right = Node(10)
root.right.right = Node(14)
root.right.right.left = Node(19)
root.right.right.right = Node(2)
pairwiseSwapLeaves(root, [None])
inorder(root)
print()