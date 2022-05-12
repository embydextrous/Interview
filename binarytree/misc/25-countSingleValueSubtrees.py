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
        return True
    left = countUtil(root.left, count)
    right = countUtil(root.right, count)
    if left and right:
        if root.left is None and root.right is None:
            count[0] += 1
            return True
        elif root.left is None and root.right.data == root.data:
            count[0] += 1
            return True
        elif root.right is None and root.left.data == root.data:
            count[0] += 1
            return True
        elif root.data == root.left.data and root.data == root.right.data:
            count[0] += 1
            return True
    return False

def count(root):
    count = [0]
    countUtil(root, count)
    return count[0]
    
root = Node(5)
root.left = Node(4)
root.right = Node(5)
root.left.left = Node(4)
root.left.right = Node(4)
root.right.right = Node(5)

print(count(root))