'''
Given an unsorted array arr[0..n-1] of size n, find the minimum length subarray arr[s..e] such that sorting 
this subarray makes the whole array sorted. 
Examples: 
1) If the input array is [10, 12, 20, 30, 25, 40, 32, 31, 35, 50, 60], your program should be able to find 
that the subarray lies between the indexes 3 and 8.
2) If the input array is [0, 1, 15, 25, 6, 7, 30, 40, 50], your program should be able to find that the 
subarray lies between the indexes 2 and 5.
'''
def findSubArray(a):
    n = len(a)
    x = -1
    for i in range(n-1):
        if a[i] > a[i+1]:
            x = i
            break
    if x == -1:
        return []
    y = -1
    for i in range(n-1, 0, -1):
        if a[i] < a[i-1]:
            y = i
            break
    maxi = max(a[x:y+1])
    mini = min(a[x:y+1])
    for i in range(x):
        if a[i] > mini:
            x = i
            break
    for i in range(n-1, y, -1):
        if a[i] < maxi:
            y = i
            break
    return a[x:y+1]

a = [5, 4, 3, 2, 1]
print(findSubArray(a))

