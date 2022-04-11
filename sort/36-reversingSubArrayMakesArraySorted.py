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
    maxi = -10 ** 9
    for i in range(n - 1):
        if a[i] > a[i + 1]:
            x = i
            break
        maxi = max(maxi, a[i])
    if x == -1:
        print("Already Sorted")
        return True
    y = -1
    mini = 10 ** 9
    for i in range(n - 1, x, -1):
        if a[i] < a[i - 1]:
            y = i
            break
        mini = min(mini, a[i])
    if y == -1:
        print("Impossible")
        return False
    print(x, y, maxi, mini)
    for i in range(x, y + 1):
        print(a[i], maxi, mini)
        if a[i] < maxi or a[i] > mini:
            return False
        if i != x:
            if a[i] > a[i-1]:
                return False
    return True

a = [1, 4, 7, 9, 8, 6]
print(check(a))
    
    
