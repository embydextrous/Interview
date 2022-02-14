from bst import Node, insert

# Assuming a < b
def lca(root, a, b):
    if root == None or root.data == a or root.data == b:
        return root
    if root.data > a and root.data < b:
        return root
    if root.data > b:
        return lca(root.left, a, b)
    return lca(root.right, a, b)

# Assuming key exists
def distance(root, x):
    if root.data == x:
        return 0
    if root.data > x:
        return 1 + distance(root.left, x)
    return 1 + distance(root.right, x)

# Assuming lca will not be None
def distanceBetweenNodes(root, a, b):
    _lca = lca(root, a, b)
    return distance(_lca, a) + distance(_lca, b)

'''
            20
         /      \
       10       30
      /  \     /  \
     5    15  25   35

'''
root = Node(20)
insert(root, 10)
insert(root, 5)
insert(root, 15)
insert(root, 30)
insert(root, 25)
insert(root, 35)
a, b = 5, 10
print(distanceBetweenNodes(root, a, b))