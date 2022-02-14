class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.leftSize = 0

def insert(root, data):
    if root is None:
        return Node(data)
    if data <= root.data:
        root.left = insert(root.left, data)
        root.leftSize += 1
    else:
        root.right = insert(root.right, data)
    return root

'''
                5
              /   \
            1      9
             \    / \
              4  7  13
             / \
            4   5
           /
          3  
[5, 1, 4, 4, 5, 9, 7, 13, 3]
5 - 5
1 - 0
4 - 2
4 - 1
5 - 0
9 - 1
7 - 0
13 - 0
3 - 0
'''

def rank(root, x):
    if root.data == x:
        return root.leftSize
    if x < root.data:
        if root.left:
            return rank(root.left, x)
        return -1
    if root.right:
        rightSize = rank(root.right, x)
        if rightSize == -1:
            return -1
        else:
            return root.leftSize + 1 + rightSize
    return -1

a = [5, 1, 4, 4, 5, 9, 7, 13, 3]
root = Node(5)
for i in range(1, len(a)):
    insert(root, a[i])
x = 9
print(rank(root, x))