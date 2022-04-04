from tree import Node

# Similar logic for n'th inorder and n'th preorder element

def nthNode(root, n):
    if root:
        nthNode(root.left, n)
        nthNode(root.right, n)
        n[0] -= 1
        if n[0] == 0:
            print(root.data)

root = Node(3)
root.left = Node(2)
root.right = Node(4)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.right = Node(5)

nthNode(root, [4])
