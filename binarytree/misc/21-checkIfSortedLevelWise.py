from tree import Node
# https://www.geeksforgeeks.org/check-if-a-binary-tree-is-sorted-level-wise-or-not/

'''
Given a binary tree. The task is to check if the binary tree is sorted level-wise or not. 
A binary tree is level sorted if max( i-1th level) is less than min(ith level). 
Examples: 
 

Input :        1 
              / \
             /   \
            2     3
           / \   / \
          /   \ /   \
         4    5 6    7
Output : Sorted
'''
import sys
from tree import Node

def checkSorted(root):
    if root is None:
        return True
    q1, q2 = [root], []
    maxi = root.data
    while len(q1) > 0:
        maxLastLevel = -sys.maxsize-1
        while len(q1) > 0:
            node = q1.pop(0)
            if node.data < maxi:
                return False
            maxLastLevel = max(maxLastLevel, node.data)
            if node.left:
                q2.append(node.left)
            if node.right:
                q2.append(node.right)
        maxi = maxLastLevel
        q1, q2 = q2, q1
    return True

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
print(checkSorted(root))