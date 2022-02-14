from bst import Node, insert
import sys

# Also see, https://www.geeksforgeeks.org/maximum-element-two-nodes-bst/ (In this case we don't need to find lca)
# assuming that a and b exists in tree and are different and a < b
def lca(root, a, b):
    if root is None or root.data == a or root.data == b:
        return root
    if root.data > a and root.data < b:
        return root
    if root.data > b:
        return lca(root.left, a, b)
    return lca(root.right, a, b)

def findMaxNodeOnPath(root, x, maxNode):
    if root.data == x:
        return
    maxNode[0] = max(maxNode[0], root.data)
    if root.data > x:
        findMaxNodeOnPath(root.left, x, maxNode)
    else:
        findMaxNodeOnPath(root.right, x, maxNode)

# assuming a < b
def findMaxNode(root, a, b):
    _lca = lca(root, a, b)
    maxNode = [-sys.maxsize-1]
    if _lca.data == b:
        findMaxNodeOnPath(_lca.left, a, maxNode)
    elif _lca.data == a:
        findMaxNodeOnPath(_lca.right, b, maxNode)
    else:
        findMaxNodeOnPath(_lca, b, maxNode)
    return maxNode[0]


'''
                    18
                   /  \
                 9      36 
                /  \
               6    12
              / \   /
             1   8 10 
'''
a = [18, 36, 9, 6, 12, 10, 1, 8]
root = Node(a[0])
for i in range(1, len(a)):
    insert(root, a[i])
a = 9
b = 10
print(findMaxNode(root, a, b))
