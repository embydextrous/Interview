from tree import Node

def findDiff(root):
    if root is None:
        return 0
    q1, q2 = [root], []
    i = 1
    diff = 0
    while len(q1) > 0:
        while len(q1):
            node = q1.pop(0)
            diff += i * node.data
            if node.left:
                q2.append(node.left)
            if node.right:
                q2.append(node.right)
        i *= -1
        q1, q2 = q2, q1
    return diff



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
print(findDiff(root))