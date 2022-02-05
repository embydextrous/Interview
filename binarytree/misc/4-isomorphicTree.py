# https://www.geeksforgeeks.org/tree-isomorphism-problem/
from tree import Node, preorder

def isIsomorphic(a, b):
    if a is None and b is None:
        return True
    if a is None or b is None:
        return False
    if a.data != b.data:
        return False
    return (isIsomorphic(a.left, b.left) and isIsomorphic(a.right, b.right)) or (isIsomorphic(a.left, b.right) and isIsomorphic(a.right, b.left))


n1 = Node(1)
n1.left = Node(2)
n1.right = Node(3)
n1.left.left = Node(4)
n1.left.right = Node(5)
n1.right.left = Node(6)
n1.left.right.left = Node(7)
n1.left.right.right = Node(8)
 
n2 = Node(1)
n2.left = Node(3)
n2.right = Node(2)
n2.right.left = Node(4)
n2.right.right = Node(5)
n2.left.right = Node(6)
n2.right.right.left = Node(8)
n2.right.right.right  = Node(7)

print(isIsomorphic(n1, n2))
