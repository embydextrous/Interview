'''
Given an array of sorted integers. We need to find the closest value to the given number. 
Array may contain duplicate values and negative numbers. 

Examples:  

Input : arr[] = {1, 2, 4, 5, 6, 6, 8, 9}
             Target number = 11
Output : 9
9 is closest to 11 in given array

Input :arr[] = {2, 5, 6, 7, 8, 8, 9}; 
       Target number = 4
Output : 5
'''
def findClosest(a, l, r, x):
    if l == r:
        return a[l]
    if l + 1 == r:
        return a[l] if abs(x - a[l]) <= abs(x - a[r]) else a[r]
    m = l + (r - l) // 2
    if a[m] == x:
        return a[m]
    if a[m] < x:
        if a[m+1] > x:
            return a[m] if abs(x - a[m]) <= abs(x - a[m+1]) else a[m+1]
        else:
            return findClosest(a, m + 1, r, x)
    else:
        if a[m-1] < x:
            return a[m] if abs(x - a[m]) <= abs(x - a[m-1]) else a[m-1]
        else:
            return findClosest(a, l, m - 1, x)

a = [1, 2, 4, 5, 6, 6, 8, 9]
for i in range(11):
    print("Closest to " + str(i) + " is " + str(findClosest(a, 0, len(a)-1, i)))