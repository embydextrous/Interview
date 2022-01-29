from tree import Node

def verticalOrder(root):
    if root is None:
        return
    q = [(root, 0)]
    d = {}
    mini, maxi = 0, 0
    while len(q) > 0:
        (node, i) = q.pop(0)
        mini = min(mini, i)
        maxi = max(maxi, i)
        if i in d:
            d[i].append(node.data)
        else:
            d[i] = [node.data]
        if node.left:
            q.append((node.left, i - 1))
        if node.right:
            q.append((node.right, i + 1))
    for i in range(mini, maxi + 1):
        for x in d[i]:
            print(x, end = " ")
        print()
    



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

verticalOrder(root)