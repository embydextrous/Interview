'''
Given an array that represents Inorder Traversal, find all possible Binary Trees with the given Inorder 
traversal and print their preorder traversals.
Examples: 
 

Input:   in[] = {3, 2};
Output:  Preorder traversals of different possible Binary Trees are:
         3 2
         2 3
Below are different possible binary trees
    3        2
     \      /
      2    3

Input:   in[] = {4, 5, 7};
Output:  Preorder traversals of different possible Binary Trees are:
          4 5 7 
          4 7 5 
          5 4 7 
          7 4 5 
          7 5 4 
Below are different possible binary trees
  4         4           5         7       7
   \          \       /   \      /       /
    5          7     4     7    4       5
     \        /                  \     /
      7      5                    5   4 
'''
from tree import Node, preorder

def getTrees(arr, start, end):
    trees = []
    if start > end:
        trees.append(None)
        return trees
    for i in range(start, end + 1):
        lTrees = getTrees(arr, start, i - 1)
        rTrees = getTrees(arr, i + 1, end)
        for left in lTrees:
            for right in rTrees:
                node = Node(arr[i])
                node.left, node.right = left, right
                trees.append(node)
    return trees


ino = [4, 5, 7]
trees = getTrees(ino, 0, len(ino) - 1)
for root in trees:
    preorder(root)
    print()