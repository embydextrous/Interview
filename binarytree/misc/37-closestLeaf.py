from tree import Node
from collections import deque

'''
          10
       /     \
     12       13
    /       /     \
   99    14       15    
        /   \     /  \
       21   22   23   24
       /\   /\   /\   /\
      1 2  3 4  5 6  7  8
'''

def closestLeafDown(root):
    if root is None:
        return -1
    q = deque([[root, 0]])
    while len(q) > 0:
        node, d = q.popleft()
        if node.left is None and node.right is None:
            return d
        if node.left:
            q.append([node.left, d + 1])
        if node.right:
            q.append([node.right, d + 1])

def closestLeafUtil(root, node, dist, leaf):
    if root is None:
        return -1
    if root == node:
        x = closestLeafDown(root)
        if x < dist[0]:
            dist[0] = x
            leaf[0] = root
        return 0
    dl = closestLeafUtil(root.left, node, dist, leaf)
    if dl != -1:
        x = dl + 2 + closestLeafDown(root.right)
        if x < dist[0]:
            dist[0] = x
            leaf[0] = root
        return dl + 1
    dr = closestLeafUtil(root.right, node, dist, leaf)
    if dr != -1:
        x = dr + 2 + closestLeafDown(root.left)
        if x < dist[0]:
            dist[0] = x
            leaf[0] = root
        return dr + 1
    return -1

def closestLeaf(root, node):
    dist = [10**9]
    leaf = [None]
    closestLeafUtil(root, node, dist, leaf)
    print(dist[0])
    return leaf[0]

root = Node(1)
root.left = Node(12)
root.left.left = Node(99)
root.left.left.left = Node(781)
root.right = Node(13)
 
root.right.left = Node(14)
root.right.right = Node(15)
 
root.right.left.left = Node(21)
root.right.left.right = Node(22)
root.right.right.left = Node(23)
root.right.right.right = Node(24)
 
root.right.left.left.left = Node(1)
root.right.left.left.right = Node(2)
root.right.left.right.left = Node(3)
root.right.left.right.right = Node(4)
root.right.right.left.left = Node(5)
root.right.right.left.right = Node(6)
root.right.right.right.left = Node(7)
root.right.right.right.right = Node(8)

closestLeaf(root, root.right)

