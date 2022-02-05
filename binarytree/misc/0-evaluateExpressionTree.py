from tree import Node

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
 
'''
    root = None
 
    # creating a sample tree
    root = node('+')
    root.left = node('*')
    root.left.left = node('5')
    root.left.right = node('4')
    root.right = node('-')
    root.right.left = node('100')
    root.right.right = node('/')
    root.right.right.left = node('20')
    root.right.right.right = node('2')
    print evaluateExpressionTree(root)
'''