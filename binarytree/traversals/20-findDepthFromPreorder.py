'''
Given preorder of a binary tree, calculate its depth(or height) [starting from depth 0]. The preorder is 
given as a string with two possible characters. 

    l - denotes the leaf
    n - denotes internal node

The given tree can be seen as a full binary tree where every node has 0 or two children. The two children 
of a node can n or l or mix of both.
Examples :  

Input  : nlnll
Output : 2
Explanation :

Input  : nlnnlll
Output : 3


'''
def findDepthUtil(preorder, index):
    if index[0] >= len(preorder) or preorder[index[0]] == 'l':
        return 0
    index[0] += 1
    leftDepth = findDepthUtil(preorder, index)
    index[0] += 1
    rightDepth = findDepthUtil(preorder, index)
    return max(leftDepth, rightDepth) + 1

def findDepth(preorder):
    return findDepthUtil(preorder, [0])

print(findDepth("nlnnlll"))