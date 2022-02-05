from tree import Node

def longestPathSameValueUtil(root, result):
    if root is None:
        return 0
    left = longestPathSameValueUtil(root.left, result)
    right = longestPathSameValueUtil(root.right, result)
    leftMax = rightMax = 0
    if root.left and root.left.data == root.data:
        leftMax = left + 1
    if root.right and root.right.data == root.data:
        rightMax = right + 1
    result[0] = max(result[0], leftMax + rightMax)
    return max(leftMax, rightMax)

def longestPathSameValue(root):
    if root is None:
        return 0
    result = [0]
    longestPathSameValueUtil(root, result)
    return result[0]

'''
              4
             / \
            4   4
           / \   \
          4   9   5
'''
root = Node(4)
root.left = Node(4)
root.right = Node(4)
root.left.left = Node(4)
root.left.right = Node(9)
root.right.right = Node(5)

print(longestPathSameValue(root))