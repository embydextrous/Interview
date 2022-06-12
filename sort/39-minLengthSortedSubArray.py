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
    for i in range(1, n):
        if a[i] < a[i-1]:
            x = i - 1
            break
    if x == -1:
        print("Already sorted.")
        return []
    y = -1
    for i in range(n - 2, x - 1, -1):
        if a[i] > a[i+1]:
            y = i + 1
            break
    maxi = mini = a[x]
    for i in range(x + 1, y + 1):
        if a[i] < mini:
            mini = a[i]
        elif a[i] > maxi:
            maxi = a[i]
    while x > 0 and a[x-1] > mini:
        x -= 1
    while y < n - 1 and a[y+1] < maxi:
        y += 1
    return a[x:y+1]

a = [0, 1, 15, 25, 6, 7, 30, 40, 50]
print(findSubArray(a))

