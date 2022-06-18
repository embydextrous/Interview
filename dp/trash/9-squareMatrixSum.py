'''
Given N which is the size of the N X N spiral matrix of the form: 
 

16 15 14 13
5  4  3  12
6  1  2  11
7  8  9  10
The task is to find the sum of the diagonal elements of this matrix.
Examples: 
 

Input: N = 3
Output: 25
5 4 3
6 1 2
7 8 9
The sum of elements along its two diagonals will be 
1 + 3 + 7 + 5 + 9 = 25

Input: N = 5
Output: 101
'''
def diagonalSum(N):
    result, d, next = 0, 0, 0
    if N % 2 == 0:
        result = 0
        d = 1
    else:
        result = 1
        d = 2
    next = result + d
    print(result, next, d)
    for i in range(N // 2):
        result += 4 * next + 6 * d
        d += 2
        next = next + 3 * (d - 2) + d
    return result

N = 5
print(diagonalSum(N))