def printNodes(root, x):
    if root and root.data < x:
        print(root.data, end = " ")
        printNodes(root.left, x)
        printNodes(root.right, x)

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

'''
                   2
                /     \
               3        15
            /    \     / \
           5       4  45  80
          / \     / \
         6   150 77 120
'''
root = Node(2)
root.left = Node(3)
root.left.left = Node(5)
root.left.left.left = Node(6)
root.left.left.right = Node(150)
root.left.right = Node(4)
root.left.right.left = Node(77)
root.left.right.right = Node(120)
root.right = Node(15)
root.right.left = Node(45)
root.right.right = Node(80)

printNodes(root, 80)
print()