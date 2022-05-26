from bst import Node, insert
import sys

# Also see, https://www.geeksforgeeks.org/maximum-element-two-nodes-bst/ (In this case we don't need to find lca)
# assuming that a and b exists in tree and are different and a < b
def findMaxNode(root, a, b):
    if root is None:
        return
    if root.data == a:
        while root.right:
            root = root.right
        return root.data
    if root.data == b:
        return b
    if root.data > a and root.data < b:
        while root.right:
            root = root.right
        return root.data
    if root.data < a:
        return findMaxNode(root.right, a, b)
    return findMaxNode(root.left, a, b)


'''
                    18
                   /  \
                 9      36 
                /  \
               6    12
              / \   /
             1   8 10 
'''
a = [18, 36, 9, 6, 12, 10, 1, 8]
root = Node(a[0])
for i in range(1, len(a)):
    insert(root, a[i])
a = 1
b = 8
print(findMaxNode(root, a, b))
