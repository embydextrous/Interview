# https://www.geeksforgeeks.org/sorting-rows-matrix-ascending-order-followed-sorting-columns-descending-order/

# Similar Question - https://www.geeksforgeeks.org/sort-matrix-row-wise-column-wise/ (same solution except no reversal [::-1] in line 23)
'''
Given a matrix, sort the rows of matrix in ascending order followed by sorting the columns in descending order. 
Examples : 
 

Input : a[3][3] = {{1, 2, 3},
                  {4, 5, 6}, 
                  {7, 8, 9}};
Output : 7 8 9
         4 5 6
         1 2 3

Input : a[3][3] = {{3, 2, 1},
                  {9, 8, 7}, 
                  {6, 5, 4}};
Output : 7 8 9
         4 5 6
         1 2 3
'''


from matrix import printS

def transpose(m):
    R, C = len(m), len(m[0])
    tp = []
    for i in range(C):
        a = []
        for j in range(R):
            a.append(m[j][i])
        tp.append(a)
    return tp

def sort(m):
    for row in m:
        row.sort()
    tp = transpose(m)
    printS(tp)
    for i in range(len(tp)):
        tp[i] = sorted(tp[i])[::-1]
    return transpose(tp)


M = [[3, 2, 1], [9, 8, 7], [6, 5, 4]]
S = sort(M)
printS(S)
