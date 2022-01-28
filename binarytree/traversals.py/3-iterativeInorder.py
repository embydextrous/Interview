from tree import Node

def inorder(root):
    s = []
    current = root
    while True:
        if current:
            s.append(current)
            current = current.left
        else:
            if len(s) == 0:
                break
            node = s.pop()
            print(node.data, end = " ")
            current = node.right
    print()

    

root = Node(3)
root.left = Node(2)
root.right = Node(4)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.right = Node(5)

inorder(root)