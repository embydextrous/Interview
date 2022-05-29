# https://www.geeksforgeeks.org/leaf-nodes-preorder-binary-search-tree/
def printLeaves(pre):
    n = len(pre)
    i = 0
    s = []
    for x in pre:
        isLeafFound = False
        while len(s) > 0 and s[-1] < x:
            item = s.pop()
            if len(s) > 0 and s[-1] < x and not isLeafFound:
                isLeafFound = True
                print(item, end = " ")
        s.append(x)
    if len(s) > 0:
        print(s[-1], end = " ")
    print()

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
