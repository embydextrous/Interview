from bst import Node, insert

def kSmallestSumUtil(root, k, sum):
    if root:
        kSmallestSumUtil(root.left, k, sum)
        k[0] -= 1
        if k[0] >= 0:
            sum[0] += root.data
        kSmallestSumUtil(root.right, k, sum)

def kSmallestSum(root, k):
    if root is None:
        return 0
    sum = [0]
    kSmallestSumUtil(root, [k], sum)
    return sum
'''
            7
          /   \
         3     12
        / \    /
       1   5  8
          /    \
         4      11
'''

root = Node(7)
insert(root, 3)
insert(root, 12)
insert(root, 5)
insert(root, 1)
insert(root, 4)
insert(root, 8)
insert(root, 11)

print(kSmallestSum(root, 5))
