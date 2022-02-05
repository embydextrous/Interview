from tree import Node
# https://www.geeksforgeeks.org/find-count-of-singly-subtrees/
'''
Given a binary tree, write a program to count the number of Single Valued Subtrees. 
A Single Valued Subtree is one in which all the nodes have same value. Expected time complexity is O(n).
Example: 

Input: root of below tree
              5
             / \
            1   5
           / \   \
          5   5   5
Output: 4
There are 4 subtrees with single values.


Input: root of below tree
              5
             / \
            4   5
           / \   \
          4   4   5                
Output: 5
There are five subtrees with single values.
'''

def countUtil(root, count):
    if root is None:
        return (True, -1)
    isLeftSingly, leftValue = countUtil(root.left, count)
    if not isLeftSingly:
        return
    isRightSingly, rightValue = countUtil(root.right, count)
    if not isRightSingly:
        return
    if isLeftSingly and isRightSingly:
        isSingly = False
        if leftValue == -1 and rightValue == -1:
            count[0] += 1
            isSingly = True
        elif leftValue == -1 and rightValue == root.data:
            count[0] += 1
            isSingly = True
        elif rightValue == -1 and leftValue == root.data:
            count[0] += 1
            isSingly = True
        elif leftValue == rightValue and rightValue == root.data:
            count[0] += 1
            isSingly = True
    return (isSingly, root.data)

def countSubtrees(root):
    if root is None:
        return 0
    count = [0]
    countUtil(root, count)
    return count[0]
    
root = Node(5)
root.left = Node(4)
root.right = Node(5)
root.left.left = Node(4)
root.left.right = Node(4)
root.right.right = Node(5)

print(countSubtrees(root))