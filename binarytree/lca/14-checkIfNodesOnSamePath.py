from tree import Node

def lcaUtil(root, a, b, visitedA, visitedB):
    if root is None:
        return None
    if root == a or root == b:
        if root == a:
            visitedA[0] = True
        if root == b:
            visitedB[0] = True
        return root
    rootA = lcaUtil(root.left, a, b, visitedA, visitedB)
    rootB = lcaUtil(root.right, a, b, visitedA, visitedB)
    if rootA and rootB:
        return root
    return rootA if rootA else rootB

def lca(root, a, b):
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

def checkIfOnSamePath(root, a, b):
    if root is None:
        return False
    _lca = lca(root, a, b)
    return _lca == a or _lca == b

'''
              1
           /     \
          2       3
        /   \    /  \
       4     5  6    7 
'''
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print(checkIfOnSamePath(root, root.left, root.right))