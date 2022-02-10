from bst import Node

def check(root, s, result):
    if root:
        if root.data not in s:
            result[0] = False
            return
        check(root.left, s, result)
        check(root.right, s, result)
        
def fillSet(root, s):
    if root:
        s.add(root.data)
        fillSet(root.left, s)
        fillSet(root.right, s)
        
def checkIfSame(a, b):
    s = set()
    fillSet(a, s)
    result = [True]
    check(b, s, result)
    return result[0]

# First BST
root1 = Node(15)
root1.left = Node(10)
root1.right = Node(20)
root1.left.left = Node(5)
root1.left.right = Node(12)
root1.right.right = Node(25)
     
# Second BST
root2 = Node(15)
root2.left = Node(11)
root2.right = Node(20)
root2.left.left = Node(5)
root2.left.left.right = Node(10)
root2.right.right = Node(25)


print(checkIfSame(root1, root2))