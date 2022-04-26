from tree import Node

def leafToLeafPathWithLargestSumUtil(root, maxSum, maxPath):
    if root is None:
        return (0, [])
    lSum, lPath = leafToLeafPathWithLargestSumUtil(root.left, maxSum, maxPath)
    rSum, rPath = leafToLeafPathWithLargestSumUtil(root.right, maxSum, maxPath)
    if lSum <= rSum:
        mPath = rPath
    else:
        mPath = lPath
    if root.data + lSum + rSum > maxSum[0]:
        maxSum[0] = root.data + lSum + rSum
        maxPath[0] = lPath[:]
        maxPath[0].append(root.data)
        maxPath[0].extend(reversed(rPath))
    mPath.append(root.data)
    return (root.data + max(lSum, rSum), mPath)
    
def leafToLeafPathWithLargestSum(root):
    maxSum = [0]
    maxPath = [[]]
    leafToLeafPathWithLargestSumUtil(root, maxSum, maxPath)
    return (maxSum[0], maxPath[0])
    
root = Node(8)
root.left = Node(3)
root.left.left = Node(51)
root.left.right = Node(16)
root.left.right.left = Node(54)
root.left.right.right = Node(7)
root.right = Node(10)
root.right.right = Node(14)
root.right.right.left = Node(19)
root.right.right.right = Node(2)

'''
        8
      /   \
     3     10
   /   \     \
  1    16     14
      /  \   /  \
     4    7 19   2
'''
print(leafToLeafPathWithLargestSum(root))