'''
Input: parent[] = {1, 5, 5, 2, 2, -1, 3}
Output: root of below tree
          5
        /  \
       1    2
      /    / \
     0    3   4
         /
        6 
'''
from tree import Node, inorder

# parent - { 1, 5, 5, 2, 2, -1, 3 }
# nodes - { 0, 1, 2, 3, 4, 5, 3}
# idx - 1
def constructUtil(parent, nodes, idx, root):
    for i in range(len(parent)):
        if parent[idx] != -1:
            if nodes[parent[idx]].left is None:
                nodes[parent[idx]].left = nodes[idx]
            else:
                nodes[parent[idx]].right = nodes[idx]

def construct(parent):
    nodes = [Node(i) for i in range(len(parent))]
    root = None
    for i in range(len(parent)):
        if parent[i] != -1:
            if nodes[parent[i]].left is None:
                nodes[parent[i]].left = nodes[i]
            else:
                nodes[parent[i]].right = nodes[i]
        else:
            root = nodes[i]
    return root

parent = [1, 5, 5, 2, 2, -1, 3]
inorder(construct(parent))
print()



