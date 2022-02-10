from bst import Node, insert

# https://www.geeksforgeeks.org/print-bst-keys-in-given-range-o1-space/ (Use Morris Traversal)
def printKeysInRange(root, k1, k2):
    if root:
        if root.data >= k1 and root.data <= k2:
            print(root.data, end = " ")
            printKeysInRange(root.left, k1, k2)
            printKeysInRange(root.right, k1, k2)
        if root.data > k2:
            printKeysInRange(root.left, k1, k2)
        if root.data < k1:
            printKeysInRange(root.right, k1, k2)

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
printKeysInRange(root, 9, 22)
print()
