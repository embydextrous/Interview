# https://www.geeksforgeeks.org/sum-matrix-element-element-integer-division-row-column/

'''
Consider a N X N matrix where each element is divided by a column number (integer division), i.e. 
mat[i][j] = floor((i+1)/(j+1)) where 0 <= i < n and 0 <= j < n. The task is to find the sum of all matrix elements.

Examples :  

Input  : N = 2
Output : 4
2 X 2 matrix with given constraint:
1 0
2 1
Sum of matrix element: 4

Input  : N = 3
Output : 9
1 0 0
2 1 0
3 1 1

Input  : N = 4
Output : 17
1 0 0 0
2 1 0 0
3 1 1 0
4 2 1 1

Input  : N = 5
Output : 27
1 0 0 0 0
2 1 0 0 0
3 1 1 0 0
4 2 1 1 0
5 2 1 1 1
'''

def findSum(n):
    sum = 0
    for i in range(n):
        if i == 0:
            sum += (n * (n + 1)) // 2
        else:
            s = n - i
            toAdd = 1
            while s > 0:
                multiplier = min(i + 1, s)
                sum += toAdd * multiplier
                toAdd += 1
                s -= multiplier
    return sum

print(findSum(5))
