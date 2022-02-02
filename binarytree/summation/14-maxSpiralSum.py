from tree import Node
import sys

def maxSpiralSum(root):
    if root is None:
        return 0
    s1, s2 = [root], []
    maxSoFar = -sys.maxsize-1
    maxEndingHere = 0
    while len(s1) > 0 or len(s2) > 0:
        while len(s1) > 0:
            node = s1.pop()
            maxEndingHere = maxEndingHere + node.data
            if maxEndingHere > maxSoFar:
                maxSoFar = maxEndingHere
            if maxEndingHere < 0:
                maxEndingHere = 0
            if node.right:
                s2.append(node.right)
            if node.left:
                s2.append(node.left)
        while len(s2) > 0:
            node = s2.pop()
            maxEndingHere = maxEndingHere + node.data
            if maxEndingHere > maxSoFar:
                maxSoFar = maxEndingHere
            if maxEndingHere < 0:
                maxEndingHere = 0
            if node.left:
                s1.append(node.left)
            if node.right:
                s1.append(node.right)
    return maxSoFar


'''
         -2
       /    \
     -3       4
    /  \     /  \
   5    1  -2   -1
  /               \
 -3                2  
'''
root = Node(-2)
root.left = Node(-3)
root.right = Node(4)
root.left.left = Node(5)
root.left.right = Node(1)
root.right.left = Node(-2)
root.right.right = Node(-1)
root.left.left.left = Node(-3)
root.right.right.right = Node(2)
print(maxSpiralSum(root))