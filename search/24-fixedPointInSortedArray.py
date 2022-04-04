# https://www.geeksforgeeks.org/find-a-fixed-point-in-a-given-array/

'''
Given an array of n distinct integers sorted in ascending order, 
write a function that returns a Fixed Point in the array, if there is any Fixed Point present in array,
else returns -1. Fixed Point in an array is an index i such that arr[i] is equal to i. 
Note that integers in array can be negative. 
Examples: 
 

  Input: arr[] = {-10, -5, 0, 3, 7}
  Output: 3  // arr[3] == 3 

  Input: arr[] = {0, 2, 5, 8, 17}
  Output: 0  // arr[0] == 0 


  Input: arr[] = {-10, -5, 3, 4, 7, 9}
  Output: -1  // No Fixed Point
''' 

# If mid is fixedPoint return.
# If mid + 1 <= a[r], search in right subArray
# if mid - 1 >= a[l], search in left subArray
def fixedPoint(a, l, r):
    if l > r:
        return -1
    m = l + (r - l) // 2
    if a[m] == m:
        return m
    res = -1
    if m + 1 <= a[r]:
        res = fixedPoint(a, m + 1, r)
    if res != -1:
        return res
    if m - 1 >= a[l]:
        return fixedPoint(a, l, m - 1)
    return -1

a = [-10, -5, 3, 4, 7, 9]
print(fixedPoint(a, 0, len(a) - 1))