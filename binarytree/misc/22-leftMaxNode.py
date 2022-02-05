from tree import Node

def maxLeftNodeUtil(root, maxNode, isLeft):
    if root is None:
        return
    if isLeft:
        maxNode[0] = max(maxNode[0], root.data)
    maxLeftNodeUtil(root.left, maxNode, True)
    maxLeftNodeUtil(root.right, maxNode, False)

def maxLeftNode(root):
    if root is None:
        return None
    maxNode = [root.data]
    maxLeftNodeUtil(root, maxNode, True)
    return maxNode[0]

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

print(maxLeftNode(root))

