from bst import Node, insert

def ceil(root, key):
    if root is None:
        return -1
    if key == root.data:
        return root.data
    if key > root.data:
        k = ceil(root.right, key)
        if k == -1:
            return root.data
        else:
            return k
    return ceil(root.left, key)

def floor(root, key):
    if root is None:
        return -1
    if key == root.data:
        return root.data
    if key < root.data:
        k = floor(root.left, key)
        if k == -1:
            return root.data
        else:
            return k
    return floor(root.right, key)

root = Node(5)
insert(root, 2)
insert(root, 1)
insert(root, 3)
insert(root, 12)
insert(root, 9)
insert(root, 21)
insert(root, 19)
insert(root, 25)

print(ceil(root, 24))
print(floor(root, 24))