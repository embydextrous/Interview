from tree import Node

def size(root):
    if root is None:
        return 0
    return 1 + size(root.left) + size(root.right)

def checkUtil(root, n):
    if root is None:
        return False
    if size(root) == n // 2:
        return True
    return checkUtil(root.left, n) or checkUtil(root.right, n)

def check(root):
    n = size(root)
    if n % 2 == 0:
        return checkUtil(root, size(root))
    return False

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

print(check(root))