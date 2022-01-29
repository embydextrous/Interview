from tree import Node, inorder

def checkDuplicateUtil(root, subTrees, result):
    if root is None:
        return '_'
    if root.left is None and root.right is None:
        return root.data
    left = checkDuplicateUtil(root.left, subTrees, result)
    right = checkDuplicateUtil(root.right, subTrees, result)
    s = left + root.data + right
    if len(s) == 3:
        if s in subTrees:
            result[0] = root
        subTrees.add(s)
    return s

def checkDuplicate(root):
    tree = [None]
    checkDuplicateUtil(root, set(), tree)
    inorder(tree[0])
    print()
    return tree[0] != None

root = Node('A')
root.left = Node('B')
root.right = Node('C')
root.left.left = Node('D')
root.left.right = Node('E')
root.right.right = Node('B')
root.right.right.right = Node('E')
root.right.right.left = Node('D')
print(checkDuplicate(root))

'''
Input:
               A
             /   \ 
           B       C
         /   \       \    
        D     E       B     
                     /  \    
                    D    E
'''

    