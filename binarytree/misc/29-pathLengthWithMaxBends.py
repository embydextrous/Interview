from tree import Node

def pathLengthWithMaxBends(root, bendLen, maxBends, parentDirection, direction):
    if root is None:
        return
    if direction != parentDirection:
        bendLen += 1
    if root.left is None and root.right is None:
        maxBends[0] = max(maxBends[0], bendLen)
    pathLengthWithMaxBends(root.left, bendLen, maxBends, direction, "l")
    pathLengthWithMaxBends(root.right, bendLen, maxBends, direction, "r")

def maxBendsLength(root):
    if root is None:
        return 0
    maxBends = [0]
    pathLengthWithMaxBends(root.left, 0, maxBends, "-", "l")
    pathLengthWithMaxBends(root.right, 0, maxBends, "-", "r")
    return maxBends[0]

'''
            10
          /    \ 
         8      2
        / \    /
       3   5  2
               \
                1
               /
              9       
'''

root = Node(10)
root.left = Node(8)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(5)
root.right.left = Node(2)
root.right.left.right = Node(1)
root.right.left.right.left = Node(9)

print(maxBendsLength(root))