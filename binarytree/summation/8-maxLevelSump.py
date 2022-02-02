from tree import Node

# https://www.geeksforgeeks.org/maximum-sum-tree-adjacent-levels-not-allowed/

def maxLevelSum(root):
    if root is None:
        return 0
    q1, q2 = [root], []
    maxSum = root.data
    while len(q1) > 0:
        s = 0
        while len(q1) > 0:
            node = q1.pop(0)
            s += node.data
            if node.left:
                q2.append(node.left)
            if node.right:
                q2.append(node.right)
        maxSum = max(maxSum, s)
        q1, q2 = q2, q1
    return maxSum
        
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

print(maxLevelSum(root))


