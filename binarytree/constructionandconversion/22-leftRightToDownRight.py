from tree import Node

# https://www.geeksforgeeks.org/convert-left-right-representation-bianry-tree-right/

'''
Given a binary tree in left-right representation as below 

                       1
                    /    \
                   2      3
                        /   \
                       4     5
                      /     /  \
                     6     7    8 

Convert the structure of the tree to down-right representation like the below tree. 

            1
            |
            2 -- 3
                 |
                 4 -- 5
                 |    |
                 6    7 -- 8 
'''

def convert(root):
    if root is None:
        return
    convert(root.left)
    convert(root.right)
    if root.left is None:
        root.left = root.right
    else:
        root.left.right = root.right
    root.right = None

def downRightTraversal(root):
    if root:
        print(root.data, end = " ")
        downRightTraversal(root.left)
        downRightTraversal(root.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.right.left = Node(4)
root.right.right = Node(5)
root.right.left.left = Node(6)
root.right.right.left = Node(7)
root.right.right.right = Node(8)

downRightTraversal(root)
print()