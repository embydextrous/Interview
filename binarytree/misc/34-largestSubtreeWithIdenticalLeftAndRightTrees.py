from tree import Node

# https://www.geeksforgeeks.org/find-largest-subtree-having-identical-left-and-right-subtrees/
def largestIdenticalSubtreesUtil(root, maxSize, maxNode):
    if root is None:
        return ("", 0)
    left = largestIdenticalSubtreesUtil(root.left, maxSize, maxNode)
    right = largestIdenticalSubtreesUtil(root.right, maxSize, maxNode)
    if left[0] == right[0] and left[1] + right[1] + 1 > maxSize[0]:
        maxSize[0] = left[1] + right[1] + 1
        maxNode[0] = root
    print(left[0] + "<" + str(root.data) + ">" + right[0])
    return (left[0] + "<" + str(root.data) + ">" + right[0], 1 + left[1] + right[1])

def largestIdenticalSubtrees(root):
    if root is None:
        return None
    maxSize = [0]
    maxNode = [None]
    largestIdenticalSubtreesUtil(root, maxSize, maxNode)
    return maxNode[0]

root = Node(50)
root.left = Node(10)
root.right = Node(60)
root.left.left = Node(5)
root.left.right = Node(20)
root.right.left = Node(70)
root.right.left.left = Node(65)
root.right.left.right = Node(80)
root.right.right = Node(70)
root.right.right.left = Node(65)
root.right.right.right = Node(80)

'''
            50
         /      \
        10       60
       /  \     /   \
      5   20   70    70
               / \   / \
             65  80 65  80
'''

print(largestIdenticalSubtrees(root).data)