from tree import Node
import sys

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

def closestLeafDown(root, dist, result):
    if root is None:
        return
    q1, q2 = [root], []
    print(root.data, dist)
    while len(q1) > 0:
        while len(q1) > 0:
            node = q1.pop(0)
            if node.left is None and node.right is None and dist < result[1]:
                result[0] = node
                result[1] = dist
                return
            if node.left:
                q2.append(node.left)
            if node.right:
                q2.append(node.right)
        q1, q2 = q2, q1
        dist += 1

def closestLeafUp(root, node, result):
    if root is None:
        return -1
    if root == node:
        closestLeafDown(root, 0, result)
        return 0
    dl = closestLeafUp(root.left, node, result)
    if dl != -1:
        closestLeafDown(root.right, dl + 2, result)
        return 1 + dl
    dr = closestLeafUp(root.right, node, result)
    if dr != -1:
        closestLeafDown(root.left, dr + 2, result)
        return 1 + dr
    return -1

def closestLeaf(root, node):
    if root is None:
        print(None)
    result = [None, sys.maxsize]
    closestLeafUp(root, node, result)
    print("The closest leaf to {} is {} at a distance of {}".format(node.data, result[0].data, result[1]))

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

