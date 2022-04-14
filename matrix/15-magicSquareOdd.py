# https://www.geeksforgeeks.org/magic-square/
'''
A magic square of order n is an arrangement of n^2 numbers, usually distinct integers, in a square, such that 
the n numbers in all rows, all columns, and both diagonals sum to the same constant. A magic square contains 
the integers from 1 to n2. 

The constant sum in every row, column and diagonal are called the magic constant or magic sum, M. 
The magic constant of a normal magic square depends only on n and has the following value: M = n(n2+1)/2

For normal magic squares of order n = 3, 4, 5, ...,
the magic constants are: 15, 34, 65, 111, 175, 260, ... 
In this post, we will discuss how programmatically we can generate a magic square of size n. 
This approach only takes into account odd values of n and doesn't work for even numbers. Before we go further, 
consider the below examples:

Magic Square of size 3
-----------------------
  2   7   6
  9   5   1
  4   3   8
Sum in each row & each column = 3*(32+1)/2 = 15


Magic Square of size 5
----------------------
  9   3  22  16  15
  2  21  20  14   8
 25  19  13   7   1
 18  12   6   5  24
 11  10   4  23  17
Sum in each row & each column = 5*(52+1)/2 = 65


Magic Square of size 7
----------------------
 20  12   4  45  37  29  28
 11   3  44  36  35  27  19
  2  43  42  34  26  18  10
 49  41  33  25  17   9   1
 40  32  24  16   8   7  48
 31  23  15  14   6  47  39
 22  21  13   5  46  38  30
Sum in each row & each column = 7*(72+1)/2 = 175
'''
from matrix import printS

def createMagicSquare(n):
    result = [[0 for i in range(n)] for i in range(n)]
    i, j = n // 2, n-1
    k = 1
    while True:
        if result[i][j] == 0:
            result[i][j] = k
            k += 1
            i -= 1
            j += 1
        else:
            i += 1
            j -= 2
        if i == -1 and j == n:
            i, j = 0, n - 2
        else:
            i = i % n if i >= 0 else n + i
            j = j % n if j >= 0 else n + j
        if k == n * n + 1:
            break
    return result


printS(createMagicSquare(5))