# https://www.geeksforgeeks.org/sum-numbers-formed-root-leaf-paths/

'''
Given a binary tree, where every node value is a Digit from 1-9 .Find the sum of all the numbers which 
are formed from root to leaf paths.
For example consider the following Binary Tree. 
 

          6
       /      \
     3          5
   /   \          \
  2     5          4  
      /   \
     7     4
  There are 4 leaves, hence 4 root to leaf paths:
   Path                    Number
  6->3->2                   632
  6->3->5->7               6357
  6->3->5->4               6354
  6->5>4                    654   
Answer = 632 + 6357 + 6354 + 654 = 13997 
'''
from tree import Node

def sumRootToLeafUtil(root, pathNum, sum):
    if root is None:
        return
    pathNum = 10 * pathNum + root.data
    if root.left is None and root.right is None:
        sum[0] += pathNum
    sumRootToLeafUtil(root.left, pathNum, sum)
    sumRootToLeafUtil(root.right, pathNum, sum)

def sumRootToLeaf(root):
    if root is None:
        return 0
    sum = [0]
    sumRootToLeafUtil(root, 0, sum)
    return sum[0]

root = Node(6)
root.left = Node(3)
root.right = Node(5)
root.left.left = Node(2)
root.left.right = Node(5)
root.right.right = Node(4)
root.left.right.left = Node(7)
root.left.right.right = Node(4)
print(sumRootToLeaf(root))