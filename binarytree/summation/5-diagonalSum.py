from tree import Node

def printDiagonalSum(root):
    if root is None:
        print(0, end = " ")
    q1, q2 = [root], []
    while len(q1) > 0:
        sum = 0
        while len(q1) > 0:
            node = q1.pop(0)
            sum += node.data
            if node.left:
                q2.append(node.left)
            if node.right:
                q1.append(node.right)
        print(sum)
        q1, q2 = q2, q1
    print()   



'''
        8
      /   \
     3     10
   /   \     \
  1    16     14
      /  \   /  \
     4    1 1    2
'''
root = Node(8)
root.left = Node(3)
root.left.left = Node(1)
root.left.right = Node(16)
root.left.right.left = Node(4)
root.left.right.right = Node(1)
root.right = Node(10)
root.right.right = Node(14)
root.right.right.left = Node(1)
root.right.right.right = Node(2)

printDiagonalSum(root)