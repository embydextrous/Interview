from tree import Node

'''
Given a simple expression tree, consisting of basic binary operators i.e., + , - ,* and / and some integers,
evaluate the expression tree.

            +
          /   \
        *       -
      /   \   /   \    
     5    4  100  20  
'''

def eval(root):
    if root is None:
        return 0
    # Leafs are numbers so simply return
    if root.left is None and root.right is None:
        return int(root.data)
    # evaluate left and right subtree
    lVal = eval(root.left)
    rVal = eval(root.right)
    # perform operation
    if root.data == '+':
        return lVal + rVal
    elif root.data == '-':
        return lVal - rVal
    elif root.data == '*':
        return lVal * rVal
    else:
        return lVal / rVal


root = Node('+')
root.left = Node('*')
root.left.left = Node('5')
root.left.right = Node('4')
root.right = Node('/')
root.right.left = Node('100')
root.right.right = Node('20')
print(eval(root))