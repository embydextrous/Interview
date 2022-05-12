from collections import deque

class Node:
    def __init__(self, data, parent):
        self.data = data
        self.left = None
        self.right = None
        self.parent = parent

def findRight(root):
    if root is None:
        return None
    if root.parent is None:
        return None
    upd = 1
    parent = root.parent
    while parent:
        if parent.right == root:
            upd += 1
        elif parent.left == root:
            q = deque([[parent, 0]])
            while len(q) > 0:
                node, d = q.popleft()
                if d == upd:
                    return node.data
                if node.left and node.left != root:
                    q.append([node.left, d + 1])
                if node.right:
                    q.append([node.right, d + 1])
            upd += 1
        root, parent = parent, parent.parent

'''
             1
            / \
           2   3
          /  \  \
         4    6  5
        /      \  \
       7        9  8
       /         \
      10         12
'''

root = Node(1, None)
root.left = Node(2, root)
root.right = Node(3, root)
root.left.left = Node(4, root.left)
root.left.right = Node(6, root.left)
root.left.left.left = Node(7, root.left.left)
root.left.left.left.left = Node(10, root.left.left.left)
root.left.right.right = Node(9, root.left.right)
root.right.right = Node(5, root.right)
root.right.right.right = Node(8, root.right.right)
root.right.right.right.right = Node(12, root.right.right.right)

print(findRight(root.left.left.left.left))
    
    
    
        