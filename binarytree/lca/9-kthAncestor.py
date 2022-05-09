from tree import Node

def kthAncestorUtil(root, a, k, result):
    if root is None:
        return -1
    if root == a:
        return 0
    dl = kthAncestorUtil(root.left, a, k, result)
    if dl != -1:
        if dl + 1 == k:
            result[0] = root.data
        return dl + 1
    dr = kthAncestorUtil(root.right, a, k, result)
    if dr != -1:
        if dr + 1 == k:
            result[0] = root.data
        return dr + 1
    return -1

def kthAncestor(root, a, k):
    result = [None]
    kthAncestorUtil(root, a, k, result)
    return result[0]

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
print(kthAncestor(root, root.left.right.right, 1))
