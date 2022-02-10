from bst import Node, insert

def countUtil(root, k1, k2, count):
    if root:
        if root.data >= k1 and root.data <= k2:
            count[0] += 1
            countUtil(root.left, k1, k2, count)
            countUtil(root.right, k1, k2, count)
        elif root.data < k1:
            countUtil(root.right, k1, k2, count)
        else:
            countUtil(root.left, k1, k2, count)

def count(root, k1, k2):
    c = [0]
    countUtil(root, k1, k2, c)
    return c[0]

'''
            12
          /    \
         7     21
       /  \    / \
      2    8  16  24
       \    \   \
        6    11  18   
'''
root = Node(12)
insert(root, 7)
insert(root, 8)
insert(root, 11)
insert(root, 2)
insert(root, 6)
insert(root, 21)
insert(root, 16)
insert(root, 18)
insert(root, 24)

print(count(root, 1, 24))