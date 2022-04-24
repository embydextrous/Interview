import heapq
from tree import Node

def printLevelsSorted(root):
    if root is None:
        return
    h1, h2 = [[root.data, root]], []
    while len(h1) > 0:
        while len(h1):
            data, node = heapq.heappop(h1)
            print(data, end = " ")
            if node.left:
                heapq.heappush(h2, [node.left.data, node.left])
            if node.right:
                heapq.heappush(h2, [node.right.data, node.right])
        print()
        h1, h2 = h2, h1


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
root.right.right = Node(14)
root.right.right.left = Node(19)
root.right.right.right = Node(2)

printLevelsSorted(root)