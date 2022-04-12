# https://www.geeksforgeeks.org/check-reversing-sub-array-make-array-sorted/
'''
Given an array of distinct n integers. The task is to check whether reversing one sub-array make the array 
sorted or not. If the array is already sorted or by reversing a subarray once make it sorted, print “Yes”, 
else print “No”.
Examples: 
 
Input : arr [] = {1, 2, 5, 4, 3}
Output : Yes
By reversing the subarray {5, 4, 3}, 
the array will be sorted.

Input : arr [] = { 1, 2, 4, 5, 3 }
Output : No
'''
def check(a):
    n = len(a)
    x = -1
    for i in range(n - 1):
        if a[i] > a[i + 1]:
            x = i
            break
    if x == -1:
        return (True, "Already Sorted")
    y = -1
    for i in range(n - 1, x, -1):
        if a[i] < a[i - 1]:
            y = i
            break
    mini = min(a[x:y+1])
    maxi = max(a[x:y+1])
    for i in range(x):
        if a[i] > mini:
            x = i
            break
    for i in range(n-1, y, -1):
        if a[i] < maxi:
            y = i
            break
    for i in range(x, y):
        if a[i] < a[i+1]:
            return (False, None)
    return (True, a[x:y+1])

a = [5, 4, 3, 2, 1]
print(check(a))
    
    
