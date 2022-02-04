from tree import Node

def find(root, a):
    if root is None:
        return False
    return root == a or find(root.left, a) or find(root.right, a)

def lcaUtil(root, a, b, vA, vB):
    if root is None:
        return None
    if root == a:
        vA[0] = True
        return root
    if root == b:
        vB[0] = True
        return root
    rootA = lcaUtil(root.left, a, b, vA, vB)
    rootB = lcaUtil(root.right, a, b, vA, vB)
    if rootA and rootB:
        return root
    return rootA if rootA else rootB

def lca(root, a, b):
    if root is None:
        return None
    vA = [False]
    vB = [False]
    _lca = lcaUtil(root, a, b, vA, vB)
    if (vA[0] and vB[0]) or (vA[0] and find(root, b)) or (vB[0] and find(root, b)):
        return _lca
    return None

def printPath(root, path, a):
    if root is None:
        return
    path.append(root.data)
    if root == a:
        print(path)
        return
    printPath(root.left, path, a)
    printPath(root.right, path, a)
    path.pop()

def printCommonPath(root, a, b):
    l = lca(root, a, b)
    if l is None:
        print("No common path.")
    printPath(root, [], l)

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

printCommonPath(root, root.right.right.left, None)