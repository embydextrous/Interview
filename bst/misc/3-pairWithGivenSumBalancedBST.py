from bst import Node, insert

# https://www.geeksforgeeks.org/print-common-nodes-in-two-binary-search-trees/

def pairWithSum(root, sum):
    s1 = []
    s2 = []
    a, b = root, root
    while True:
        if a or b:
            if a:
                s1.append(a)
                a = a.left
            if b:
                s2.append(b)
                b = b.right
        else:
            if len(s1) == 0 or len(s2) == 0:
                break
            a = s1.pop()
            b = s2.pop()
            if a.data + b.data == sum:
                print(a.data, b.data)
                return True
            elif a.data + b.data < sum:
                a = a.right
                s2.append(b)
                b = None
            else:
                b = b.left
                s1.append(a)
                a = None
    print()

'''
            5
          /   \
         1     10
        / \    /
       0   4  8
               \
                9    
'''

root1 = Node(5) 
root1 = insert(root1, 1) 
root1 = insert(root1, 10) 
root1 = insert(root1, 0) 
root1 = insert(root1, 4) 
root1 = insert(root1, 8) 
root1 = insert(root1, 9) 
  

print(pairWithSum(root1, 12))