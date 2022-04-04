# https://www.geeksforgeeks.org/find-the-maximum-element-in-an-array-which-is-first-increasing-and-then-decreasing/

'''
Given an array of integers which is initially increasing and then decreasing, 
find the maximum value in the array. 
Examples : 
 
Input: arr[] = {8, 10, 20, 80, 100, 200, 400, 500, 3, 2, 1}
Output: 500

Input: arr[] = {1, 3, 50, 10, 9, 7, 6}
Output: 50

Corner case (No decreasing part)
Input: arr[] = {10, 20, 30, 40, 50}
Output: 50

Corner case (No increasing part)
Input: arr[] = {120, 100, 80, 20, 0}
Output: 120
'''
def findMax(a, l, r):
    if l == r:
        return a[l]
    if l + 1 == r:
        return max(a[l], a[r])
    m = l + (r - l) // 2
    if a[m - 1] < a[m] and a[m + 1] < a[m]:
        return a[m]
    if a[m - 1] < a[m] and a[m] < a[m + 1]:
        return findMax(a, m + 1, r)
    return findMax(a, l, m - 1)

a = [120, 100, 80, 20, 0]
print(findMax(a, 0, len(a) - 1))