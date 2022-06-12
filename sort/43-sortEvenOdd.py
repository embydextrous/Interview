'''
Given an array of integers (both odd and even), sort them in such a way that the first part of the array 
odd numbers sorted in descending order, rest portion contains even numbers sorted in ascending order.

Examples: 

Input  : arr[] = {1, 2, 3, 5, 4, 7, 10}
Output : arr[] = {7, 5, 3, 1, 2, 4, 10}

Input  : arr[] = {0, 4, 5, 3, 7, 2, 1}
Output : arr[] = {7, 5, 3, 1, 0, 2, 4} 
'''
def sort(a):
    a.sort()
    l = 0
    n = len(a)
    for i in range(n):
        if a[i] % 2 == 1:
            x = a[i]
            for j in range(i, l, -1):
                a[j] = a[j-1]
            a[l] = x
            l += 1
    r = l - 1
    l = 0
    while l < r:
        a[l], a[r] = a[r], a[l]
        l += 1
        r -= 1

a = [0, 4, 5, 3, 7, 2, 1]
sort(a)
print(a)
