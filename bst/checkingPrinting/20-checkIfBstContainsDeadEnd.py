from bst import Node, insert
import sys

# https://www.geeksforgeeks.org/simple-recursive-solution-check-whether-bst-contains-dead-end/

MAXI = sys.maxsize
MINI = 1

def checkUtil(root, low, high, result):
    if root:
        if low == high:
            result[0] = True
        checkUtil(root.left, low, root.data - 1, result)
        checkUtil(root.right, root.data + 1, high, result)

def check(root):
    result = [False]
    checkUtil(root, MINI, MAXI, result)
    return result[0]

'''
                8
               / \
              5   11
             / \
            2   7
             \
              3 
               \
                4   
'''

root = Node(8)
insert(root, 5)
insert(root, 2)
insert(root, 3)
insert(root, 7)
insert(root, 11)
insert(root, 4)

print(check(root))
