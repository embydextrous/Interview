from tree import Node
'''
A tree is a Continuous tree if in each root to leaf path, the absolute difference between keys of 
two adjacent is 1. We are given a binary tree, we need to check if the tree is continuous or not.

Examples: 

Input :              3
                    / \
                   2   4
                  / \   \
                 1   3   5
Output: "Yes"

// 3->2->1 every two adjacent node's absolute difference is 1
// 3->2->3 every two adjacent node's absolute difference is 1
// 3->4->5 every two adjacent node's absolute difference is 1

Input :              7
                    / \
                   5   8
                  / \   \
                 6   4   10
Output: "No"

// 7->5->6 here absolute difference of 7 and 5 is not 1.
// 7->5->4 here absolute difference of 7 and 5 is not 1.
// 7->8->10 here absolute difference of 8 and 10 is not 1.

Recommended: P
'''

def isContinuousTree(root):
    if root is None:
        return True
    if root.left is None and root.right is None:
        return True
    if root.left is None:
        return abs(root.data - root.right.data) == 1 and isContinuousTree(root.right)
    if root.right is None:
        return abs(root.data - root.left.data) == 1 and isContinuousTree(root.left)
    return abs(root.data - root.left.data) == 1 and abs(root.data - root.right.data) == 1 and isContinuousTree(root.left) and isContinuousTree(root.right)


root = Node(3)
root.left = Node(2)
root.right = Node(4)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.right = Node(5)

print(isContinuousTree(root))
