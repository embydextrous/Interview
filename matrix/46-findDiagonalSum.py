# https://www.geeksforgeeks.org/sum-diagonals-spiral-odd-order-square-matrix/
'''
    Difficulty Level : Easy
    Last Updated : 21 Apr, 2021

We have given a spiral matrix of odd-order, in which we start with the number 1 as center and moving to the 
right in a clockwise direction.
Examples : 
 

Input : n = 3 
Output : 25
Explanation : spiral matrix = 
7 8 9
6 1 2
5 4 3
The sum of diagonals is 7+1+3+9+5 = 25

Input : n = 5
Output : 101
Explanation : spiral matrix of order 5
21 22 23 23 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13
The sum of diagonals is 21+7+1+3+13+
25+9+5+17 = 101
'''
# n is odd
def findDiagonalSum(n):
    s = 1
    i = 1
    step = 0
    while i < n * n:
        step = step + 2
        for j in range(4):
            i += step
            s += i
    return s

n = 5
print(findDiagonalSum(n))
