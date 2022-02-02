from tree import Node

def largestSumSubtreeUtil(root, maxSum):
    if root is None:
        return 0
    lSum = largestSumSubtreeUtil(root.left, maxSum)
    rSum = largestSumSubtreeUtil(root.right, maxSum)
    maxSum[0] = max(maxSum[0], root.data + lSum + rSum)
    return root.data + lSum + rSum


def largestSumSubtree(root):
    maxSum = [0]
    largestSumSubtreeUtil(root, maxSum)
    return maxSum[0]

'''
        8
      /   \
     3     10
   /   \     \
  1    -46    14
      /  \   /  \
     4    1 1    2
'''
root = Node(8)
root.left = Node(3)
root.left.left = Node(1)
root.left.right = Node(-46)
root.left.right.left = Node(4)
root.left.right.right = Node(1)
root.right = Node(10)
root.right.right = Node(14)
root.right.right.left = Node(1)
root.right.right.right = Node(2)

print(largestSumSubtree(root))
