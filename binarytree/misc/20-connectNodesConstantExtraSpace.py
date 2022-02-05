from tree import Node

def getNextRight(root):
    next = root.next
    while next:
        if next.left:
            return next.left
        if next.right:
            return next.right
        next = next.next
    return None

def connect(root):
    if root is None:
        return
    while root:
        node = root
        while node:
            if node.left:
                if node.right:
                    node.left.next = node.right
                else:
                    node.left.next = getNextRight(node)
            if node.right:
                node.right.next = getNextRight(node)
            node = node.next
        if root.left:
            root = root.left
        elif root.right:
            root = root.right
        else:
            root = getNextRight(root)

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

connect(root)

current = root
while current:
    print(current.data, end = " ")
    current = current.next
print()

current = root.left
while current:
    print(current.data, end = " ")
    current = current.next
print()

current = root.left.left
while current:
    print(current.data, end = " ")
    current = current.next
print()

current = root.left.right.left
while current:
    print(current.data, end = " ")
    current = current.next
print()