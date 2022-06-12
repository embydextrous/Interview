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
    for i in range(1, n):
        if a[i] < a[i-1]:
            x = i - 1
            break
    if x == -1:
        print("Already sorted.")
        return False
    y = -1
    for i in range(n - 2, x - 1, -1):
        if a[i] > a[i+1]:
            y = i + 1
            break
    print(x, y)
    for i in range(y, x, -1):
        if a[y] > a[y-1]:
            return False
    return True

x = 0
y = 4
    

a = [1, 2, 2, 2, 4, 4, 4, 2, 4, 4, 5]
print(check(a))
    
    
