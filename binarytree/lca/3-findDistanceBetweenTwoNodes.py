from tree import Node

def findDistance(root, node, distance):
    if root is None:
        return -1
    if root == node:
        return distance
    lDistance = findDistance(root.left, node, distance + 1)
    if lDistance != -1:
        return lDistance
    return findDistance(root.right, node, distance + 1)

def lcaUtil(root, a, b, visitedA, visitedB):
    if root is None:
        return None
    if root == a:
        visitedA[0] = True
        return root
    if root == b:
        visitedB[0] = True
        return root
    rootA = lcaUtil(root.left, a, b, visitedA, visitedB)
    rootB = lcaUtil(root.right, a, b, visitedA, visitedB)
    if rootA and rootB:
        return root
    return rootA if rootA else rootB

def lca(root, a, b):
    if root is None:
        return None
    visitedA = [False]
    visitedB = [False]
    _lca = lcaUtil(root, a, b, visitedA, visitedB)
    if (visitedA[0] and visitedB[0]) or (visitedA[0] and find(root, b)) or (visitedB[0] and find(root, a)):
        return _lca
    return None

def find(root, a):
    if root is None:
        return False
    return root == a or find(root.left, a) or find(root.right, a)

def findDist(root, a, b):
    l = lca(root, a, b)
    if l is None:
        return -1
    if l == a:
        return findDistance(a, b, 0)
    if l == b:
        return findDistance(b, a, 0)
    return findDistance(l, a, 0) + findDistance(l, b, 0)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print(findDist(root, root.left, root.right))