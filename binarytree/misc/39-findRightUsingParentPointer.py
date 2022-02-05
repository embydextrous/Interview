class Node:
    def __init__(self, data, parent):
        self.data = data
        self.left = None
        self.right = None
        self.parent = parent

def findRight(node):
    if node is None:
        return None
    if node.parent is None:
        return None
    parent = node.parent
    level = 0
    while parent:
        if parent.right == node:
            parent, node = parent.parent, parent 
            level += 1
        else:
            break
    while parent:
        if parent.right is None:
            parent = parent.parent
            level += 1
            continue
        k = 0
        q1, q2 = [parent.right], []
        while len(q1) > 0:
            while len(q1) > 0:
                noad = q1.pop(0)
                if level == k:
                    return noad
                if noad.left:
                    q2.append(noad.left)
                if noad.right:
                    q2.append(noad.right)
            k += 1
            q1, q2 = q2, q1
        level += 1
        parent = parent.parent

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

print(findRight(root.left.left.left.left).data)
    
    
    
        