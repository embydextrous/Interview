from bst import Node, inorder, insert

def printMerged(root1, root2):
    if root1 is None:
        inorder(root2)
    if root2 is None:
        inorder(root1)
    s1 = []
    s2 = []
    while root1 or root2 or len(s1) > 0 or len(s2) > 0:
        if root1 or root2:
            if root1:
                s1.append(root1)
                root1 = root1.left
            if root2:
                s2.append(root2)
                root2 = root2.left
        else:
            if len(s1) == 0:
                while len(s2) != 0:
                    root2 = s2.pop()
                    print(root2.data, end = " ")
                    inorder(root2.right)
                break
            if len(s2) == 0:
                while len(s1) != 0:
                    root1 = s1.pop()
                    print(root1.data, end = " ")
                    inorder(root1.right)
                break
            root1 = s1.pop()
            root2 = s2.pop()
            if root1.data < root2.data:
                print(root1.data, end = " ")
                s2.append(root2)
                root2 = None
                root1 = root1.right
            else:
                print(root2.data, end = " ")
                s1.append(root1)
                root1 = None
                root2 = root2.right
    print()

root1 = Node(8)
insert(root1, 3)
insert(root1, 15)
insert(root1, 10)
insert(root1, 17)
insert(root1, 14)
insert(root1, 1)
insert(root1, 7)

inorder(root1)
print()

root2 = Node(11)
insert(root2, 9)
insert(root2, 6)
insert(root2, 12)
insert(root2, 16)

inorder(root2)
print()

printMerged(root1, root2)