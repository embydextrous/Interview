from tree import Node

def lcaUtil(root, a, b):
    if root is None:
        return None
    if root == a or root == b:
        return root
    rootA = lcaUtil(root.left, a, b)
    rootB = lcaUtil(root.right, a, b)
    if rootA and rootB:
        return root
    return rootA if rootA else rootB

def lca(root, a, b):
    _lca = lcaUtil(root, a, b)
    if _lca == a:
        return a if find(a, b) else None
    if _lca == b:
        return b if find(b, a) else None
    return _lca

def find(root, a):
    if root is None:
        return False
    return root == a or find(root.left, a) or find(root.right, a)


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

print(lca(root, root.left, root.right.right).data)