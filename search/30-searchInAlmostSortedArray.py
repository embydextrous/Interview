# https://www.geeksforgeeks.org/search-almost-sorted-array/

'''
Given an array which is sorted, but after sorting some elements are moved to either of the adjacent 
positions, i.e., arr[i] may be present at arr[i+1] or arr[i-1]. 
Write an efficient function to search an element in this array. Basically the element arr[i] can 
only be swapped with either arr[i+1] or arr[i-1].
For example consider the array {2, 3, 10, 4, 40}, 4 is moved to next position and 10 is moved 
to previous position.
Example : 
 

Input: arr[] =  {10, 3, 40, 20, 50, 80, 70}, key = 40
Output: 2 
Output is index of 40 in given array

Input: arr[] =  {10, 3, 40, 20, 50, 80, 70}, key = 90
Output: -1
-1 is returned to indicate element is not present
'''
def search(a, l, r, x):
    if l > r:
        return -1
    m = l + (r - l) // 2
    if a[m] == x:
        return m
    if m > l and a[m - 1] == x:
        return m - 1
    if m < r and a[m + 1] == x:
        return m + 1
    if a[m] > x:
        return search(a, l, m - 2, x)
    return search(a, m + 2, r, x)

a = [10, 3, 40, 20, 50, 80, 70]
x = 90
print(search(a, 0, len(a) - 1, x))