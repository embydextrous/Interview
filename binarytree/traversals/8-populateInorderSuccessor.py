from tree import Node

# Similar Question - Find inorder successor or inorder predecessor

def populateInorderSuccessor(root):
    inorderUtil(root, [None])

def inorderUtil(root, prev):
    if root:
        inorderUtil(root.right, prev)
        root.next = prev[0]
        prev[0] = root
        inorderUtil(root.left, prev)

def inorder(root):
    if root:
        inorder(root.left)
        nextToPrint = root.next.data if root.next else None
        print("root: " + str(root.data), "next: " + str(nextToPrint))
        inorder(root.right)

root = Node(3)
root.left = Node(2)
root.right = Node(4)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(5)
populateInorderSuccessor(root)
inorder(root)
