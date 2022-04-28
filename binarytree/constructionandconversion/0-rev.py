from tree import Node, inorder
from collections import deque

def leftChildRightSibling(root):
    if root is None:
        return
    q1, q2 = deque([[root, None]]), deque()
    while len(q1) > 0:
        while len(q1) > 0:
            node, parent = q1.popleft()
            if node.left:
                q2.append([node.left, node])
            if node.right:
                q2.append([node.right, node])
            if len(q1) > 0 and q1[0][1] == parent:
                node.right = q1[0][0]
            else:
                node.right = None
        q1, q2 = q2, q1

def traverse(root):
    if root:
        print(root.data, end = " ")
        traverse(root.left)
        traverse(root.right)
        

'''
         8
       /     
      3  -- 11
     /     / 
    -1 -1 3 - 7
'''

root = Node(8)
root.left = Node(3)
root.right = Node(11)
root.left.left = Node(-1)
root.left.right = Node(1)
root.right.left = Node(3)
root.right.right = Node(7)

leftChildRightSibling(root)
print(root.left.right.left)
traverse(root)
print()