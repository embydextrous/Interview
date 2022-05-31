#  https://www.geeksforgeeks.org/find-a-peak-in-a-given-array/

'''
Given an array of integers. Find a peak element in it. An array element is a peak if it is NOT 
smaller than its neighbours. For corner elements, we need to consider only one neighbour. 

Input: array[]= {5, 10, 20, 15}
Output: 20
The element 20 has neighbours 10 and 15,
both of them are less than 20.

Input: array[] = {10, 20, 15, 2, 23, 90, 67}
Output: 20 or 90
The element 20 has neighbours 10 and 15, 
both of them are less than 20, similarly 90 has neighbours 23 and 67.
'''
def findPeakElement(a, l, r):
    if l == r:
        return l
    if l + 1 == r:
        return l if a[l] >= a[r] else a[r]
    m = l + (r - l) // 2
    if a[m] >= a[m-1] and a[m] >= a[m+1]:
        return m
    if a[m-1] > a[m]:
        return findPeakElement(a, l, m - 1)
    return findPeakElement(a, m + 1, r)

a = [12, 11, 10, 2, 23, 90, 67]
print(findPeakElement(a, 0, len(a) - 1))