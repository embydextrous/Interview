'''
You are given an unsorted array with both positive and negative elements. You have to find 
the smallest positive number missing from the array in O(n) time using constant extra space. 
You can modify the original array.

Examples 

 Input:  {2, 3, 7, 6, 8, -1, -10, 15}
 Output: 1

 Input:  { 2, 3, -7, 6, 8, 1, -10, 15 }
 Output: 4

 Input: {1, 1, 0, -1, -2}
 Output: 2
'''


def segregateNonNegativeAndPositive(a):
    l, r = 0, len(a) - 1
    while l < r:
        if a[l] <= 0 and a[r] > 0:
            a[l], a[r] = a[r], a[l]
            r -= 1
            l += 1
        elif a[l] > 0:
            l += 1
        else:
            r -= 1

def findMinPositiveNumber(a):
    n = len(a)
    segregateNonNegativeAndPositive(a)
    print(a)
    for i in a:
        if i - 1 >= 0 and i - 1 < len(a):
            a[i-1] = -1
    for i in range(n):
        if a[i] > 0:
            return i + 1
    return n + 1

a = [2, 4, 5, 6, 7, -1, -10, 8]
print(findMinPositiveNumber(a))
        