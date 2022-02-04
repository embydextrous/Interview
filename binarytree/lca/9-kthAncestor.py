from tree import Node

def kthAncestor(root, a, k):
    if root is None:
        return -1
    if root == a:
        if k == 0:
            print(root.data)
        return 0
    lDist = kthAncestor(root.left, a, k)
    if lDist != -1 and lDist == k - 1:
        print(root.data)
    rDist = kthAncestor(root.right, a, k)
    if rDist != -1 and rDist == k - 1:
        print(root.data)
    if lDist == -1 and rDist == -1:
        return -1
    return 1 + lDist if lDist != -1 else 1 + rDist

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
root.left.right.left = Node(0)
root.left.right.right = Node(7)
root.right = Node(10)
root.right.right = Node(14)
root.right.right.left = Node(19)
root.right.right.right = Node(2)
kthAncestor(root, root.left.right.right, 3)
