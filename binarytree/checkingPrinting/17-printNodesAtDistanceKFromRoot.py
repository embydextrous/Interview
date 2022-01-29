from tree import Node

# Similar Questions
# https://www.geeksforgeeks.org/print-nodes-odd-levels-tree/
# https://www.geeksforgeeks.org/given-binary-tree-print-nodes-two-given-level-numbers/

def printNodesAtDistanceKFromRoot(root, k):
    if root:
        if k == 0:
            print(root.data, end = " ")
            return
        printNodesAtDistanceKFromRoot(root.left, k - 1)
        printNodesAtDistanceKFromRoot(root.right, k - 1)

def printNodesAtDistanceKFromRootIterative(root, k):
    if root is None:
        return
    q1, q2 = [root], []
    while len(q1) > 0 and k >= 0:
        while len(q1) > 0:
            node = q1.pop(0)
            if k == 0:
                print(node.data, end = " ")
            if node.left:
                q2.append(node.left)
            if node.right:
                q2.append(node.right)
        q1, q2 = q2, q1
        k -= 1
    print()


'''
        8
      /   \
     3     10
   /   \     \
  1    16     14
      /  \   /  \
     4    7 19   2
'''
root = Node(8)
root.left = Node(3)
root.left.left = Node(1)
root.left.right = Node(16)
root.left.right.left = Node(4)
root.left.right.right = Node(7)
root.right = Node(10)
root.right.right = Node(14)
root.right.right.left = Node(19)
root.right.right.right = Node(2)

printNodesAtDistanceKFromRootIterative(root, 3)
print()