from tree import Node

def printTopView(root):
    if root is None:
        return
    d = {}
    q = [(root, 0)]
    mini, maxi = 0, 0
    while len(q) > 0:
        (node, i) = q.pop(0)
        mini = min(mini, i)
        maxi = max(maxi, i)
        if i not in d:
            d[i] = node.data
        if node.left:
            q.append((node.left, i - 1))
        if node.right:
            q.append((node.right, i + 1))
    for i in range(mini, maxi + 1):
        print(d[i], end = " ")
    print()

def printBottomView(root):
    if root is None:
        return
    d = {}
    q = [(root, 0)]
    mini, maxi = 0, 0
    while len(q) > 0:
        (node, i) = q.pop(0)
        mini = min(mini, i)
        maxi = max(maxi, i)
        d[i] = node.data
        if node.left:
            q.append((node.left, i - 1))
        if node.right:
            q.append((node.right, i + 1))
    for i in range(mini, maxi + 1):
        print(d[i], end = " ")
    print()

"""
        1
       / \
      2   3
       \
        4
         \
          5
           \
            6
"""
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(4)
root.left.right.right = Node(5)
root.left.right.right.right = Node(6)
printTopView(root)
printBottomView(root)
