from tree import Node

def numTurnsDown(root, a, pdir, dir):
    if root is None:
        return -1
    if root == a:
        return 1 if pdir != None and pdir != dir else 0
    left = numTurnsDown(root.left, a, dir, 0)
    if left != -1:
        return left + (1 if pdir != None and pdir != dir else 0)
    right = numTurnsDown(root.right, a, dir, 1)
    if right != -1:
        return right + (1 if pdir != None and pdir != dir else 0)
    return -1

def numTurnsUtil(root, a, b, pdir, dir, result):
    if root is None:
        return -1
    if root == a:
        x = numTurnsDown(a, b, None, None)
        if x != -1:
            result[0] = x
        return 1 if pdir != None and pdir != dir else 0
    if root == b:
        x = numTurnsDown(b, a, None, None)
        if x != -1:
            result[0] = x
        return 1 if pdir != None and pdir != dir else 0
    left = numTurnsUtil(root.left, a, b, dir, 0, result)
    right = numTurnsUtil(root.right, a, b, dir, 1, result)
    print(root.data, left, right)
    if left != -1 and right != -1:
        result[0] = left + right + 1
        return result[0]
    if left == -1 and right == -1:
        return -1
    if left != -1:
        return left + (1 if pdir != None and pdir != dir else 0)
    if right != -1:
        return right + (1 if pdir != None and pdir != dir else 0)

def numTurns(root, a, b):
    result = [0]
    numTurnsUtil(root, a, b, None, None, result)
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
root.left.right.left = Node(4)
root.left.right.right = Node(7)
root.right = Node(10)
root.right.left = Node(36)
root.right.right = Node(14)
root.right.right.left = Node(19)
root.right.right.right = Node(2)

print(numTurns(root, root.left.right.left, root.right.right.left))