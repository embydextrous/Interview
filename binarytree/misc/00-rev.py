from collections import defaultdict, deque

class Node:
    def __init__(self, data, parent):
        self.data = data
        self.left = None
        self.right = None
        self.parent = parent

    def __repr__(self):
        return f"{self.data}"

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
def findRight(node):
    if node is None:
        return None
    if node.parent is None:
        return None
    upd = 1
    parent = node.parent
    while parent:
        if parent.right == node:
            upd += 1
        elif parent.left == node:
            q = deque([[parent, 0]])
            while len(q) > 0:
                noad, d = q.popleft()
                if d == upd:
                    return noad.data
                if noad.left and noad.left != node:
                    q.append([noad.left, d + 1])
                if noad.right:
                    q.append([noad.right, d + 1])
            upd += 1
        node, parent = parent, parent.parent
            

        
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

print(findRight(root.left.left.left))
