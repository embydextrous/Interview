from tree import Node

def findIfVerticalLevelSorted(root, k):
    if root is None:
        return True
    q1, q2 = [(root, 0)], []
    current = None
    while len(q1) > 0:
        while len(q1) > 0:
            (node, dist) = q1.pop(0)
            if dist == k:
                print(node.data)
                if current is None:
                    current = node.data
                elif node.data < current:
                    return False
            if node.left:
                q2.append((node.left, dist - 1))
            if node.right:
                q2.append((node.right, dist + 1))
        q1, q2 = q2, q1
    return True

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
print(findIfVerticalLevelSorted(root, 0))

