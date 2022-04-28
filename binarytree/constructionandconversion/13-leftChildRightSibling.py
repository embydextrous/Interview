from collections import deque
from tree import Node

class Noder:
    def __init__(self, data):
        self.data = data
        self.child = None
        self.next = None

def addSibling(node, data):
    if node == None:
        return None
    while node.next:
        node = node.next
    node.next = Noder(data)
    return node.next

def addChild(node, data):
    if node == None:
        return
    if node.child:
        return addSibling(node.child, data)
    else:
        node.child = Noder(data)
        return node.child

def traverse(root):
    if root:
        print(root.data, end = " ")
        traverse(root.child)
        traverse(root.next)

def convert(root):
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

def naapo(root):
    if root:
        print(root.data, end = " ")
        naapo(root.left)
        naapo(root.right)

root = Noder(10)
n1 = addChild(root, 2)
n2 = addChild(root, 3)
n3 = addChild(root, 4)
n4 = addChild(n3, 6)
n5 = addChild(root, 5)
n6 = addChild(n5, 7)
n7 = addChild(n5, 8)
n8 = addChild(n5, 9)
traverse(root)
print()

'''
         8
       /   \  
      3     11
     / \    / \
    -1 1   3   7
'''
root = Node(8)
root.left = Node(3)
root.right = Node(11)
root.left.left = Node(-1)
root.left.right = Node(1)
root.right.left = Node(3)
root.right.right = Node(7)

convert(root)
naapo(root)
print()