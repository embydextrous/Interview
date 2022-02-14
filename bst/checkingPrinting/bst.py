# https://www.geeksforgeeks.org/advantages-of-bst-over-hash-table/

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self) -> str:
        return str(self.data)

def insert(root, data):
    if root is None:
        return Node(data)
    if data < root.data:
        root.left = insert(root.left, data)
    elif data > root.data:
        root.right = insert(root.right, data)
    return root

def search(root, key):
    if root is None:
        return False
    if key == root.data:
        return True
    if key < root.data:
        return search(root.left, key)
    return search(root.right, key)

def searchIterative(root, key):
    while root:
        if root.data == key:
            return True
        elif root.data > key:
            root = root.left
        else:
            root = root.right
    return False

def delete(root, key):
    if root is None:
        return None
    if key == root.data:
        if root.left is None and root.right is None:
            return None
        if root.left is None:
            root.data = root.right.data
            root.right = None
            return root
        if root.right is None:
            root.data = root.left.data
            root.left = None
            return root
        leftMost = root.right
        while leftMost.left:
            leftMost = leftMost.left
        root.data = leftMost.data
        delete(root.right, leftMost.data)
        return root
    if key < root.data:
        root.left = delete(root.left, key)
    else:
        root.right = delete(root.right, key)
    return root
    
def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")
        
def levelOrder(root):
    if root is None:
        return
    q = [root]
    while len(q) > 0:
        node = q.pop(0)
        print(node.data, end = " ")
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    print()


'''
            7
          /   \
         3     12
        / \    /
       1   5  8
          /    \
         4      11

root = Node(7)
insert(root, 3)
insert(root, 12)
insert(root, 5)
insert(root, 1)
insert(root, 4)
insert(root, 8)
insert(root, 11)

inorder(root)
print()
preorder(root)
print()
postorder(root)
print()

print(search(root, 2))
print(search(root, 3))
print(search(root, 5))
print(search(root, 6))
print(search(root, 8))

delete(root, 4)
postorder(root)
print()

delete(root, 7)
postorder(root)
print()
'''