from tree import Node, inorder
from collections import deque
from math import ceil, log

class Node:
    def __init__(self, data):
        self.data = data
        self.bacche = []

    def __repr__(self):
        return f"{self.data}"

def postorder(root):
    if root:
        for baccha in root.bacche:
            postorder(baccha)
        print(root.data, end = " ")

def createTree(a, n, k, h, index):
    if index[0] >= n or h == 0:
        return None
    root = Node(a[index[0]])
    if h != 1 and index[0] + k <= n:
        for i in range(k):
            index[0] += 1
            root.bacche.append(createTree(a, n, k, h - 1, index))
    return root

def height(n, k):
    return ceil(log(n * (k - 1) + 1) / log(k))

a = [ 1, 2, 5, 6, 7, 3, 4]
n = len(a)
k = 3
h = height(n, k)
root = createTree(a, n, k, h, [0])
print(root.data, root.bacche)
postorder(root)
print()
