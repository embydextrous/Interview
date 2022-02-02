# https://www.geeksforgeeks.org/find-root-tree-children-id-sum-every-node-given/

'''
Consider a binary tree whose nodes have ids from 1 to n where n is number of nodes in the tree. 
The tree is given as a collection of n pairs, where every pair represents node id and sum of children ids.
Examples: 
 

Input : 1 5
        2 0
        3 0
        4 0
        5 5
        6 5
Output: 6
Explanation: In this case, two trees can 
be made as follows and 6 is the root node.
   6          6
   \         / \
    5       1   4
   / \       \
  1   4       5
 / \         / \
2   3       2   3
'''

# Simple Solution - All the nodes will be part of sum except root. So its sum(keys) - sum(values)
def findRoot(nodeSumPair):
    s = 0
    for node in nodeSumPair:
        s += node
        s -= nodeSumPair[node]
    return s

nodeSumPair = {1:5, 2:0, 3:0, 4:0, 5:5, 6:5}
print(findRoot(nodeSumPair))
