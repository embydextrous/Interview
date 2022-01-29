from tree import Node

def checkSequence(root, pat, index, n):
    if root is None or index == n:
        return False
    if root.left is None and root.right is None:
        if root.data == pat[index] and index == n - 1:
            return True
        return False
    return root.data == pat[index] and (checkSequence(root.left, pat, index + 1, n) or checkSequence(root.right, pat, index + 1, n))
    
root = Node("a")
root.left = Node("b")
root.left.left = Node("d")
root.left.right = Node("e")
root.left.right.left = Node("g")
root.left.right.right = Node("h")
root.right = Node("c")
root.right.right = Node("f")
root.right.right.left = Node("i")
root.right.right.right = Node("j")


'''
        a
      /   \
     b     c
   /   \     \
  d     e      f
       /  \   /  \
      g    h  i   j
'''

print(checkSequence(root, "abeh", 0, 4))
