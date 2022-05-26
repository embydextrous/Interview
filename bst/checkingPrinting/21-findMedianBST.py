from bst import Node, insert

def median(root):
    if root is None:
        return None
    a, b = root, root
    s1 = []
    s2 = []
    while True:
        if a or b:
            if a:
                s1.append(a)
                a = a.left
            if b:
                s2.append(b)
                b = b.right
        else:
            a = s1.pop()
            b = s2.pop()
            if a == b:
                return a.data
            if a.data > b.data:
                return (a.data + b.data) / 2
            a = a.right
            b = b.left

root = Node(50) 
insert(root, 30)
insert(root, 20)
insert(root, 40)
insert(root, 70)
insert(root, 60)
insert(root, 80)
'''
'''

print(median(root))