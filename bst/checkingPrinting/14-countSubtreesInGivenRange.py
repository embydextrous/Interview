from bst import Node, insert

def countUtil(root, k1, k2, count):
    if root is None:
        return True
    if root.data < k1:
        countUtil(root.right, k1, k2, count)
        return False
    if root.data > k2:
        countUtil(root.left, k1, k2, count)
        return False
    left = countUtil(root.left, k1, k2, count)
    right = countUtil(root.right, k1, k2, count)
    if left and right:
        count[0] += 1
    return left and right

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

print(count(root, 9, 22))