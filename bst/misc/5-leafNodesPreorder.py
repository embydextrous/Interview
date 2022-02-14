# https://www.geeksforgeeks.org/leaf-nodes-preorder-binary-search-tree/
def printLeaves(pre):
    n = len(pre)
    s = []
    i = 0
    for j in range(1, n):
        found = False
        if pre[i] > pre[j]:
            s.append(pre[i])
            print(s)
        else:
            while len(s) != 0:
                if pre[j] > s[-1]:
                    s.pop()
                    found = True
                else:
                    break
            print(s)
        if found:
            print(pre[i], end = " ")
        i += 1
    print(pre[n - 1])

'''
            12
          /    \
         7     21
       /  \    / \
      2    8  16  24
       \    \   \
        6    11  18  
       /
      4   
'''
pre = [12, 7, 2, 6, 4, 8, 11, 21, 16, 18, 24]
printLeaves(pre)
