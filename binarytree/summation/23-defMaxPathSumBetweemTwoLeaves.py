from tree import Node

def maxPathSumUtil(root, maxSum):
    if root is None:
        return 0
    lSum = maxPathSumUtil(root.left, maxSum)
    rSum = maxPathSumUtil(root.right, maxSum)
    maxSum[0] = max(maxSum[0], lSum + rSum + root.data)
    return max(lSum, rSum) + root.data

def maxPathSum(root):
    if root is None:
        return 0
    maxSum = [0]
    maxPathSumUtil(root, maxSum)
    return maxSum[0]

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
root.right.right.left.left = Node(30)
root.right.right.left.left.left = Node(32)
root.right.right.left.right = Node(31)

'''
        8
      /   \
     3     10
   /   \     \
  1    16     14
      /  \   /  \
     4    7 19   2
           /  \
          30   31
         /
        32 
'''
print(maxPathSum(root))