from bst import Node, insert
import sys

# https://www.geeksforgeeks.org/simple-recursive-solution-check-whether-bst-contains-dead-end/

MAXI = sys.maxsize
MINI = 1

def checkUtil(root, low, high):
    if root is None:
        return False
    if low == high:
        return True
    return checkUtil(root.left, low, root.data - 1) or checkUtil(root.right, root.data + 1, high)

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

print(checkUtil(root, 1, MAXI))
