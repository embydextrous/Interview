from tree import Node, inorder

def flip(root):
    if root is None:
        return
    s = []
    while root:
        s.append(root)
        root = root.left
    ret = s[-1]
    print(ret.data)
    while len(s) > 0:
        node = s.pop()
        if len(s) > 0:
            node.right = s[-1]
            node.left = s[-1].right
        else:
            node.left = None
            node.right = None
    return ret

def flip2(root, parent, result):
    if root:
        flip2(root.left, root, result)
        if result[0] is None:
            result[0] = root
        root.right = parent
        if parent:
            root.left = parent.right
        else:
            root.left = None  

'''
            1
          /   \
         2     3
        / \   / \
       4   5 6   7  
'''

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.right.left = Node(8)



inorder(flip(root))
print()
 