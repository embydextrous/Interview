# https://www.geeksforgeeks.org/find-height-binary-tree-represented-parent-array/
# Also see, https://www.geeksforgeeks.org/height-generic-tree-parent-array/

'''
A given array represents a tree in such a way that the array value gives the parent node of that particular
index. The value of the root node index would always be -1. Find the height of the tree. 
The height of a Binary Tree is the number of nodes on the path from the root to the deepest leaf node,
and the number includes both root and leaf. 
 

Input: parent[] = {1 5 5 2 2 -1 3}
Output: 4
The given array represents following Binary Tree 
         5
        /  \
       1    2
      /    / \
     0    3   4
         /
        6 
'''
def heightUtil(parent, idx, depth):
    if idx < len(parent):
        if depth[idx] != -1:
            heightUtil(parent, idx + 1, depth)
        elif parent[idx] == -1:
            depth[idx] = 0
            heightUtil(parent, idx + 1, depth)
        elif depth[parent[idx]] != -1:
            depth[idx] = depth[parent[idx]] + 1
            heightUtil(parent, idx + 1, depth)
        else:
            heightUtil(parent, parent[idx], depth)
            heightUtil(parent, idx, depth)

def height(parent):
    depth = [-1] * len(parent)
    heightUtil(parent, 0, depth)
    print(depth)
    return max(depth)

def h(parent):
    maxH = 0
    for i in range(len(parent)):
        j = i
        height = 0
        while parent[j] != -1:
            height += 1
            j = parent[j]
        maxH = max(maxH, height)
    return height

parent = [1, 5, 5, 2, 2, -1, 3]
# len(parent) = 7
# idx - 5
# depth - [-1, -1, -1, -1, -1, 0, -1]
print(height(parent))
