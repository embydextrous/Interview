from bst import Node, insert, inorder

def reversePath(root, key):
    if root is None:
        return
    path = []
    while True:
        path.append(root)
        if root.data > key:
            root = root.left
        elif root.data < key:
            root = root.right
        else:
            break
    l, r = 0, len(path) - 1
    while l < r:
        path[l].data, path[r].data = path[r].data, path[l].data
        l += 1
        r -= 1

root = Node(50)
insert(root, 30)
insert(root, 20)
insert(root, 40)
insert(root, 70)
insert(root, 60)
insert(root, 80)

inorder(root)
print()
reversePath(root, 70) 
inorder(root)
print()