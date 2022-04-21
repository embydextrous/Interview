from tree import Node

def checkPerfectUtil(root, leafLevel, lvl):
    if root.left is None and root.right is None:
        return lvl == leafLevel
    if root.left is None or root.right is None:
        return False
    return checkPerfectUtil(root.left, leafLevel, lvl + 1) and checkPerfectUtil(root.right, leafLevel, lvl + 1)

def checkPerfectBinaryTree(root):
    if root is None:
        return True
    level = 0
    current = root
    while current.left:
        level += 1
        current = current.left
    return checkPerfectUtil(root, level, 0)

'''
        1
      /   \
     2      3
   /  \    / \
  4    5  6   7
'''
root = Node(8)

root.left = Node(3)
root.right = Node(10)


root.left.left = Node(1)
root.left.right = Node(16)
root.right.left = Node(11)
root.right.right = Node(14)


root.left.left.left = Node(12)
root.left.left.right = Node(20)
root.left.right.left = Node(4)
root.left.right.right = Node(7)
root.right.left.left = Node(13)
root.right.left.right = Node(11)
root.right.right.left = Node(19)
root.right.right.right = Node(2)


print(checkPerfectBinaryTree(root))

