from tree import Node

def postorder(root):
    current = root
    visited = set()
    while current and current not in visited:
        if current.left and current.left not in visited:
            current = current.left
        elif current.right and current.right not in visited:
            current = current.right
        else:
            print(current.data, end= " ")
            visited.add(current)
            current = root
    print()

root = Node(3)
root.left = Node(2)
root.right = Node(4)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.right = Node(5)

postorder(root)