from tree import Node

def getPath(root, node, path):
    if root is None:
        return False
    path.append(root.data)
    if root == node:
        return True
    left = getPath(root.left, node, path)
    if left:
        return left
    right = getPath(root.right, node, path)
    if right:
        return right
    path.pop()
    return False
    
def sumOddNodes(root, a, b):
    if root is None:
        return 0
    path1 = []
    path2 = []
    existA = getPath(root, a, path1)
    existsB = getPath(root, b, path2)
    if not existA or not existsB:
        return 0
    while path1[0] == path2[0]:
        path1.pop(0)
        path2.pop(0)
    sum = 0
    for data in path1:
        if data % 2 == 1:
            sum += data
    for data in path2:
        if data % 2 == 1:
            sum += data
    return sum

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
print(sumOddNodes(root, root.left.right.left, root.right.right.left))

