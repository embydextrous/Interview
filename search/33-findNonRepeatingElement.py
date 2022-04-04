# https://www.geeksforgeeks.org/find-the-element-that-appears-once-in-a-sorted-array/

# https://www.geeksforgeeks.org/find-the-element-that-odd-number-of-times-in-olog-n-time/ (Same Solution works)
'''
Given a sorted array in which all elements appear twice (one after one) and one element appears only once. 
Find that element in O(log n) complexity.

Example: 

Input:   arr[] = {1, 1, 3, 3, 4, 5, 5, 7, 7, 8, 8}
Output:  4

Input:   arr[] = {1, 1, 3, 3, 4, 4, 5, 5, 7, 7, 8}
Output:  8
'''
def findNonRepeating(a, l, r):
    if l > r:
        return None
    if l == r:
        return a[l]
    m = l + (r - l) // 2
    if m % 2 == 0:
        if m == r:
            return a[m]
        elif a[m+1] == a[m]:
            return findNonRepeating(a, m + 2, r)
        return findNonRepeating(a, l, m)
    else:
        if m == l:
            return a[m]
        elif a[m-1] == a[m]:
            return findNonRepeating(a, m + 1, r)
        return findNonRepeating(a, l, m - 1)

a = [1, 1, 3, 3, 4, 5, 5, 7, 7, 8, 8]
print(findNonRepeating(a, 0, len(a) - 1))