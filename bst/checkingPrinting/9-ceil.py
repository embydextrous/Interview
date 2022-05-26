from bst import Node, insert

def floor(root, key):
    if root is None:
        return -1
    if key == root.data:
        return root.data
    if key > root.data:
        k = floor(root.right, key)
        if k == -1:
            return root.data
        else:
            return k
    return floor(root.left, key)

def ceil(root, key):
    if root is None:
        return -1
    if key == root.data:
        return root.data
    if key < root.data:
        k = ceil(root.left, key)
        if k == -1:
            return root.data
        else:
            return k
    return ceil(root.right, key)

root = Node(7)
insert(root, 3)
insert(root, 12)
insert(root, 5)
insert(root, 4)
insert(root, 8)
insert(root, 11)

for i in range(15):
    print(ceil(root, i))
#print(floor(root, 24))