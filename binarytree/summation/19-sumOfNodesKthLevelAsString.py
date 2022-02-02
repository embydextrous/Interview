# https://www.geeksforgeeks.org/sum-nodes-k-th-level-tree-represented-string/

'''
Given an integer 'K' and a binary tree in string format. 
Every node of a tree has value in range from 0 to 9. We need to find sum of elements at K-th level from root. 
The root is at level 0. 
Tree is given in the form: (node value(left subtree)(right subtree)) 

Examples: 

Input : tree = "(0(5(6()())(4()(9()())))(7(1()())(3()())))" 
        k = 2
Output : 14
Its tree representation is shown below
            0
          /   \
        5       7 
      /   \   /   \
    6      4 1     3
            \
             9
'''
def findSum(s, k):
    level = -1
    sum = 0
    for c in s:
        if c == '(':
            level += 1
        elif c == ')':
            level -= 1
        else:
            if level == k:
                sum += int(c)
    return sum

s = "(0(5(6()())(4()(9()())))(7(1()())(3()())))"
print(findSum(s, 2))
