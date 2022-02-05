# https://www.geeksforgeeks.org/number-subtrees-odd-count-even-numbers/
from tree import Node

'''
Given a binary tree, find the number of subtrees having odd count of even numbers.

Examples: 

Input :         2             
             /     \          
           1        3            
         /   \     /  \       
        4    10   8     5     
             /                
            6      
Output : 6
'''

def countSubtreesUtil(root, count):
    if root is None:
        return 0
    leftCount = countSubtreesUtil(root.left, count)
    rightCount = countSubtreesUtil(root.right, count)
    if (leftCount + rightCount + (root.data + 1) % 2) % 2 == 1:
        count[0] += 1
    return leftCount + rightCount + (root.data + 1) % 2

def countSubtrees(root):
    if root is None:
        return 0
    count = [0]
    countSubtreesUtil(root, count)
    return count[0]

root = Node(2)
root.left = Node(1)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(10)
root.right.left = Node(8)
root.right.right = Node(5)
root.left.right.left = Node(6)

print(countSubtrees(root))
