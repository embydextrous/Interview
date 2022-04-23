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
from tree import Node
from collections import deque

def checkSorted(root):
    if root is None:
        return True
    q1, q2 = deque([root]), deque()
    maxLastLevel = root.data
    while len(q1) > 0:
        maxCurrentLevel = q1[0].data
        while len(q1) > 0:
            node = q1.popleft()
            if node.data < maxLastLevel:
                return False
            maxCurrentLevel = max(maxCurrentLevel, node.data)
            if node.left:
                q2.append(node.left)
            if node.right:
                q2.append(node.right)
        maxLastLevel = maxCurrentLevel
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