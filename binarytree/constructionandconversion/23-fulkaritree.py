# https://www.geeksforgeeks.org/construct-full-k-ary-tree-preorder-traversal/
class Node:
    def __init__(self, data):
        self.data = data
        self.bacche = []

def createTree(a, n, h, k, ind):
    if n == 0:
        return None
    node = Node(a[ind[0]])
    for i in range(k):
        if ind[0] < n - 1 and h > 1:
            ind[0] += 1
            node.bacche.append(createTree(a, n, h - 1, k, ind))
    return node

def height(n, k):
    if n == 1:
        return 0
    h = 1
    i = 1
    m = 0
    num = 1
    while num < n:
        h += 1
        m += 1
        num += k ** m
    return h

def postorder(root):
    if root:
        for baccha in root.bacche:
            postorder(baccha)
        print(root.data, end = " ")

a = [ 1, 2, 5, 6, 7, 3, 8, 9, 10, 4]
n = len(a)
k = 3
h = height(n, k)
root = createTree(a, n, k, k, [0])
postorder(root)
print()
