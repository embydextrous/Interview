'''
Given an array of positive integers, sort the array in decreasing order of count of set bits in binary 
representations of array elements. For integers having the same number of set bits in their binary representation, 
sort according to their position in the original array i.e., a stable sort. For example, if the input array 
is {3, 5}, then the output array should also be {3, 5}. Note that both 3 and 5 have the same number set bits.

Examples:

Input: arr[] = {5, 2, 3, 9, 4, 6, 7, 15, 32};
Output: 15 7 5 3 9 6 2 4 32
Explanation:
The integers in their binary representation are:
    15 -1111
    7  -0111
    5  -0101
    3  -0011
    9  -1001
    6  -0110
    2  -0010
    4- -0100
    32 -10000
hence the non-increasing sorted order is:
{15}, {7}, {5, 3, 9, 6}, {2, 4, 32}

Input: arr[] = {1, 2, 3, 4, 5, 6};
Output: 3 5 6 1 2 4
Explanation:
    3  - 0011
    5  - 0101
    6  - 0110
    1  - 0001
    2  - 0010
    4  - 0100
hence the non-increasing sorted order is
{3, 5, 6}, {1, 2, 4}
'''
def numBits(n):
    c = 0
    while n > 0:
        fsb = n & ~(n-1)
        n = fsb ^ n
        c += 1
    return c

def calculateBits(n):
    i = 0
    while n > 0:
        n = n >> 1
        i += 1
    return i

def sort(a):
    count = [[] for i in range(calculateBits(max(a)))]
    for i in a:
        count[numBits(i) - 1].append(i)
    k = 0
    for i in range(len(count) - 1, -1, -1):
        for x in count[i]:
            a[k] = x
            k += 1

a = [5, 2, 3, 9, 4, 6, 7, 15, 32]
sort(a)
print(a)