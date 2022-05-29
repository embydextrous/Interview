from bst import Node, insert
import sys

# Also see, https://www.geeksforgeeks.org/maximum-element-two-nodes-bst/ (In this case we don't need to find lca)
# assuming that a and b exists in tree and are different and a < b
def findMaxNode(root, a, b):
    if root.data == a:
        maxi = [a]
        maxDown(root, b, maxi)
        return maxi[0]
    if root.data == b:
        return b
    if root.data > a and root.data < b:
        maxi = [root.data]
        maxDown(root, b, maxi)
        return maxi[0]
    if root.data < a:
        return findMaxNode(root.right, a, b)
    return findMaxNode(root.left, a, b)

def maxDown(root, x, maxi):
    if root.data == x:
        maxi[0] = max(maxi[0], x)
        return
    if root.data < x:
        maxDown(root.right, x, maxi)
    else:
        maxi[0] = max(maxi[0], root.data)
        maxDown(root.left, x, maxi)


'''
                    18
                   /  \
                 9      36 
                /  \    / \
               6    12 32  38
              / \   /
             1   8 10 
'''
a = [18, 36, 32, 38, 9, 6, 12, 10, 1, 8]
root = Node(a[0])
for i in range(1, len(a)):
    insert(root, a[i])
a = 6
b = 9
print(findMaxNode(root, a, b))
