def findDepthUtil(preorder, index):
    if index >= len(preorder) or preorder[index] == 'l':
        return 0
    index += 1
    leftDepth = findDepthUtil(preorder, index)
    index += 1
    rightDepth = findDepthUtil(preorder, index)
    return max(leftDepth, rightDepth) + 1

def findDepth(preorder):
    return findDepthUtil(preorder, 0)

print(findDepth("nlnnlll"))