from tree import Node

def lca(root, a, b):
    if root is None:
        return None
    if root == a or root == b:
        return root
    left = lca(root.left, a, b)
    right = lca(root.right, a, b)
    if left and right:
        return root
    return left if left else right

# Assuming both nodes are in tree
def getPath(root, node, bendHash):
    if root is None:
        return ""
    if root == node:
        return bendHash
    l = getPath(root.left, node, bendHash + "l")
    if l != "":
        return l
    r = getPath(root.right, node, bendHash + "r")
    return r

def numberTurns(root, a, b):
    if root is None:
        return 0
    _lca = lca(root, a, b)
    leftbendHash = getPath(_lca, a, "") 
    rightBendHash = getPath(_lca, b, "")
    bendCount = 0
    for i in range(1, len(leftbendHash)):
        if leftbendHash[i] != leftbendHash[i-1]:
            bendCount += 1
    for i in range(1, len(rightBendHash)):
        if rightBendHash[i] != rightBendHash[i-1]:
            bendCount += 1
    return bendCount + 1

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
root.right.left = Node(36)
root.right.right = Node(14)
root.right.right.left = Node(19)
root.right.right.right = Node(2)

print(numberTurns(root, root.left.right.left, root.right.right.left))