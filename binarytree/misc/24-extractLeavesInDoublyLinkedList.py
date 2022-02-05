from tree import Node

def extractLeavesUtil(root, tail):
    if root is None:
        return
    # As leaves will get connected
    if (root.left is None and root.right) is None or (root.left and root.left.right is root):
        tail[0].right = root
        root.left = tail[0]
        tail[0] = root
    if root.left and root.left.right != root:
        extractLeavesUtil(root.left, tail)
    extractLeavesUtil(root.right, tail)

def extractLeaves(root):
    if root is None:
        return
    head = tail = Node('*')
    extractLeavesUtil(root, [tail])
    node = head.right
    node.left = None
    return node

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

extractLeaves(root)
root = root.right.right.right
while root:
    print(root.data, end = " ")
    root = root.left
print()