from tree import Node

def checkDown(root, a, target, targetFound):
    if root is None:
        return False
    if root == a:
        return a == target or targetFound
    left = checkDown(root.left, a, target, target == root)
    if left:
        return left
    return checkDown(root.right, a, target, target == root)

def checkInPathUtil(root, a, b, target, result):
    if root is None:
        return False
    if root == a:
        if checkDown(a, b, target, False):
            result[0] = True
        return True
    if root == b:
        if checkDown(b, a, target, False):
            result[0] = True
        return True
    left = checkInPathUtil(root.left, a, b, target, result)
    right = checkInPathUtil(root.right, a, b, target, result)
    if left and right:
        result[0] = root == target
        return result[0]
    return left if left else right

def checkInPath(root, a, b, target):
    result = [False]
    checkInPathUtil(root, a, b, target, result)
    return result[0]

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

'''
        8
      /   \
     3     10
   /   \     \
  1    16     14
      /  \   /  \
     4    7 19   2
'''
print(checkInPath(root, root.left.right.left, root.right.right.left, root.left.left))

