from tree import Node

def modify(root):
    if root is None:
        return
    if root.left is None and root.right is None:
        return
    if not root.left:
        modify(root.right)
        return
    if not root.right:
        root.left, root.right = None, root.left
        modify(root.right)
        return
    rightMost = root.left
    while rightMost.right:
        rightMost = rightMost.right
    rightMost.right = root.right
    root.right = root.left
    root.left = None
    modify(root.right)

'''
      20
     /  \
    8   22
   / \    \
  4  12   25
    /  \
   10   14
   

20
   \
    8 
     \ 
      4
       \
       12
         \
          10
            \
             14
               \
                22
                  \
                   25
'''

root = Node(20)
root.left = Node(8)
root.left.left = Node(4)
root.left.right = Node(12)
root.left.right.left = Node(10)
root.left.right.right = Node(14)
root.right = Node(22)
root.right.right = Node(25)
modify(root)
while root:
    print(root.data, end = " ")
    root = root.right
print()
    
        