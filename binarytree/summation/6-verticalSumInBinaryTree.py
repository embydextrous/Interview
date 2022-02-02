from tree import Node

def verticalSum(root):
    if root is None:
        return 0
    d = {}
    q = [(root, 0)]
    mini, maxi = 0, 0
    while len(q) > 0:
        (node, i) = q.pop(0)
        mini = min(i, mini)
        maxi = max(i, maxi)
        if i in d:
            d[i] += node.data
        else:
            d[i] = node.data
        if node.left:
            q.append((node.left, i - 1))
        if node.right:
            q.append((node.right, i + 1))
    for i in range(mini, maxi + 1):
        print(str(i) + " -> " + str(d[i]))

'''
        8
      /   \
     3     10
   /   \     \
  1    16     14
      /  \   /  \
     4    1 1    2
'''
root = Node(8)
root.left = Node(3)
root.left.left = Node(1)
root.left.right = Node(16)
root.left.right.left = Node(4)
root.left.right.right = Node(1)
root.right = Node(10)
root.right.right = Node(14)
root.right.right.left = Node(1)
root.right.right.right = Node(2)

verticalSum(root)


