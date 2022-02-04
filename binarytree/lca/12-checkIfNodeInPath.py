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
    
def checkNodeInPath(root, a, b, key):
    if root is None:
        return 0
    path1 = []
    path2 = []
    existA = getPath(root, a, path1)
    existsB = getPath(root, b, path2)
    if not existA or not existsB:
        return 0
    lca = None
    while path1[0] == path2[0]:
        lca = path1.pop(0)
        path1.pop(0)
        path2.pop(0)
    if lca == key:
        return True
    for data in path1:
        if data == key:
            return True
    for data in path2:
        if data == key:
            return True
    return False

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
print(checkNodeInPath(root, root.left.right.left, root.right.right.left, 1))

