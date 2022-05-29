# https://www.geeksforgeeks.org/replace-every-element-with-the-least-greater-element-on-its-right/

'''
Given an array of integers, replace every element with the least greater element on its right side 
in the array. If there are no greater elements on the right side, replace it with -1.

Examples: 

Input: [8, 58, 71, 18, 31, 32, 63, 92, 
         43, 3, 91, 93, 25, 80, 28]
Output: [18, 63, 80, 25, 32, 43, 80, 93, 
         80, 25, 93, -1, 28, -1, -1]

        28
       /  \
      25  80
            \
            93    
'''
from bst import Node, inorder

def insertUtil(root, data, lastLeft):
    if root is None:
        return Node(data)
    if data < root.data:
        lastLeft[0] = root
        root.left = insertUtil(root.left, data, lastLeft)
    else:
        root.right = insertUtil(root.right, data, lastLeft)
    return root

def insert(root, data):
    lastLeft = [None]
    insertUtil(root, data, lastLeft)
    return lastLeft[0].data if lastLeft[0] else -1

def replaceWithLeastGreatestOnRight(a):
    n = len(a)
    root = Node(a[n-1])
    a[n-1] = -1
    for i in range(n - 2, -1, -1):
        a[i] = insert(root, a[i])

a = [8, 58, 71, 18, 31, 32, 63, 92, 43, 3, 91, 93, 25, 80, 28]
replaceWithLeastGreatestOnRight(a)
print(a)