# https://www.geeksforgeeks.org/sum-leaf-nodes-minimum-level/
from tree import Node
from collections import deque

'''
Given a binary tree containing n nodes. 
The problem is to get the sum of all the leaf nodes which are at minimum level in the binary tree.
Examples: 
 

Input : 
              1
            /   \
           2     3
         /  \   /  \
        4   5   6   7
           /     \
          8       9

Output : 11
Leaf nodes 4 and 7 are at minimum level.
Their sum = (4 + 7) = 11. 
'''
# Also see https://www.geeksforgeeks.org/sum-nodes-maximum-depth-binary-tree/ - bas last level ka sum return kar do aur koi bavaseer nahi hai

def findSum(root):
    if root is None:
        return 0
    q1, q2 = deque([root]), deque()
    while len(q1) > 0:
        sum = 0
        firstLeafFound = False
        while len(q1) > 0:
            node = q1.popleft()
            if node.left is None and node.right is None:
                firstLeafFound = True
                sum += node.data
            if node.left:
                q2.append(node.left)
            if node.right:
                q2.append(node.right)
        if firstLeafFound:
            return sum
        q1, q2 = q2, q1

'''
                1
             /     \
            2       3
          /   \    /  \ 
         4     5  6    7   
              /    \
             8      9     
'''

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.right.left = Node(8)
root.right.left.right = Node(9)

print(findSum(root))