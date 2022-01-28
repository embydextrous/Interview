from tree import Node

def inorder(root):
    current = root
    while current:
        if current.left:
            rightMost = current.left
            while rightMost.right and rightMost.right != current:
                rightMost = rightMost.right
            if rightMost.right == current:
                print(current.data, end = " ")
                rightMost.right = None
                current = current.right
            else:
                rightMost.right = current
                current = current.left
        else:
            print(current.data, end = " ")
            current = current.right
    print()

    

root = Node(3)
root.left = Node(2)
root.right = Node(4)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.right = Node(5)

inorder(root)