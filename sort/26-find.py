# https://www.geeksforgeeks.org/find-number-pairs-xy-yx/
'''
Given two arrays X[] and Y[] of positive integers, find a number of pairs such that x^y > y^x where x is an element 
from X[] and y is an element from Y[].

Examples:

    Input: X[] = {2, 1, 6}, Y = {1, 5} 
    Output: 3 
    Explanation: There are total 3 pairs where pow(x, y) is greater than pow(y, x) Pairs are (2, 1), (2, 5) and (6, 1)

    Input: X[] = {10, 19, 18}, Y[] = {11, 15, 9} 
    Output: 2 
    Explanation: There are total 2 pairs where pow(x, y) is greater than pow(y, x) Pairs are (10, 11) and (10, 15)
'''

'''
Algorithm
1. Sort both arrays.
2. For each x in first array:
        if x == 0 -> No element in second array
        if x == 1 -> count of 0's in second array
        if x == 2 -> count of 1's and 0's in second array + count of elements greater than equal to 5
        if x == 3 -> count of 0's, 1's an 2's in second array + count of elements greater than 3
        else count of 0's + count of 1's + count of elements greater than x
'''
def findNumPairs(a, b):
    a.sort()
    b.sort()
    result = 0
    countOfZeroes = count(b, 0)
    countOfOnes = count(b, 1)
    countOfTwos = count(b, 2)
    for i in a:
        if i == 1:
            print(1, countOfZeroes)
            result += countOfZeroes
        elif i == 2:
            print(2, len(b) - ceil(b, 4) + countOfZeroes + countOfOnes)
            result += len(b) - ceil(b, 4) + countOfZeroes + countOfOnes
        elif i == 3:
            print(3, len(b) - ceil(b, 3) + countOfOnes + countOfTwos + countOfZeroes)
            result += len(b) - ceil(b, 3) + countOfOnes + countOfTwos + countOfZeroes
        else:
            c = len(b) - ceil(b, i) + countOfZeroes + countOfOnes
            print(i, c)
            if c == 0:
                break
            result += len(b) - ceil(b, i) + countOfZeroes + countOfOnes
    return result

def ceilUtil(a, l, r, x):
    if l > r:
        return len(a)
    m = l + (r - l) // 2
    if a[m] > x and (l == m or a[m-1] <= x):
        return m
    if a[m] > x:
        return ceilUtil(a, l, m - 1, x)
    return ceilUtil(a, m + 1, r, x)
    
def ceil(a, x):
    return ceilUtil(a, 0, len(a) - 1, x)

def leftUtil(a, l, r, x):
    if l > r:
        return -1
    m = l + (r - l) // 2
    if a[m] == x and (m == l or a[m-1] != x):
        return m
    if a[m] >= x:
        return leftUtil(a, l, m - 1, x)
    return leftUtil(a, m + 1, r, x)
    
def left(a, x):
    return leftUtil(a, 0, len(a) - 1, x)

def rightUtil(a, l, r, x):
    if l > r:
        return -1
    m = l + (r - l) // 2
    if a[m] == x and (r == m or a[m+1] != x):
        return m
    if a[m] <= x:
        return rightUtil(a, m + 1, r, x)
    return leftUtil(a, l, m - 1, x)
    
def right(a, x):
    return rightUtil(a, 0, len(a) - 1, x)

def count(a, x):
    l = left(a, x)
    if l == -1:
        return 0
    return right(a, x) - l + 1

a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 4, 5]

print(findNumPairs(a, b))


