# https://www.geeksforgeeks.org/construct-binary-tree-string-bracket-representation/
from tree import Node, inorder

'''
Input : "4(2(3)(1))(6(5))"
Output : 4 2 3 1 6 5
Explanation :
           4
         /   \
        2     6
       / \   / 
      3   1 5   
Input : "4(2(3)(1))(6(5))"
'''
# i - 10
# s - [4]
# result - 4
# node - 6
def construct(exp):
    if len(exp) == 0:
        return
    s = [Node(exp[0])]
    i = 1
    while i < len(exp):
        if exp[i] == '(':
            i += 1
            node = Node(exp[i])
            if s[-1].left == None:
                s[-1].left = node
            else:
                s[-1].right = node
            s.append(node)
        elif exp[i] == ')':
            s.pop()
        i += 1
    return s[0]

exp = '1(2)(3)'
inorder(construct(exp))
print()