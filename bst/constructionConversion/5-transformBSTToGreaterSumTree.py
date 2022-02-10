from bst import Node, inorder

def transform(root, sum):
    if root:
        transform(root.right, sum)
        data = root.data
        root.data = sum[0]
        sum[0] += data
        transform(root.left, sum)

root = Node(11)
root.left = Node(2)
root.right = Node(29)
root.left.left = Node(1)
root.left.right = Node(7)
root.right.left = Node(15)
root.right.right = Node(40)
root.right.right.left = Node(35)
transform(root, [0])
inorder(root)
print()