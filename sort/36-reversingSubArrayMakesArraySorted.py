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
    while x > 0 and a[x] == a[x - 1]:
        x -= 1
    while y < n - 1 and a[y] == a[y + 1]:
        y += 1
    if x != 0 and a[y] < maxi:
        return False
    if y != n - 1 and a[x] > mini:
        return False
    print(x, y, maxi, mini)
    for i in range(y - 1, x - 1, -1):
        if a[i] < a[i+1]:
            return False
    return True

# if there are repeating elements and maxi == mini = p, y = last occurence of p and repeat
a = [1, 2, 2, 2, 3, 4, 2, 2]
print(check(a))
    
    
