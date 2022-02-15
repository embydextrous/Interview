from bst import Node, insert

# https://www.geeksforgeeks.org/print-common-nodes-in-two-binary-search-trees/

def printCommonNodes(a, b):
    s1 = []
    s2 = []
    while True:
        if a or b:
            if a:
                s1.append(a)
                a = a.left
            if b:
                s2.append(b)
                b = b.left
        else:
            if len(s1) == 0 or len(s2) == 0:
                break
            a = s1.pop()
            b = s2.pop()
            if a.data == b.data:
                print(a.data, end = " ")
                a = a.right
                b = b.right
            elif a.data < b.data:
                a = a.right
                s2.append(b)
                b = None
            else:
                b = b.right
                s1.append(a)
                a = None
    print()

root1 = Node(5) 
root1 = insert(root1, 1) 
root1 = insert(root1, 10) 
root1 = insert(root1, 0) 
root1 = insert(root1, 4) 
root1 = insert(root1, 8) 
root1 = insert(root1, 9) 
  
root2 = Node(10) 
root2 = insert(root2, 7) 
root2 = insert(root2, 20) 
root2 = insert(root2, 4) 
root2 = insert(root2, 9)

printCommonNodes(root1, root2)