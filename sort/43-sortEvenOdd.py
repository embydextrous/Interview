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
    l = 0
    r = len(a) - 1
    while l <= r:
        if a[l] % 2 == 0 and a[r] % 2 == 1:
            a[l], a[r] = a[r], a[l]
            l += 1
            r -= 1
        elif a[l] % 2 == 1:
            l += 1
        else:
            r -= 1
    a[:l] = sorted(a[:l])[::-1]
    a[l:] = sorted(a[l:])

a = [0, 4, 5, 3, 7, 2, 1]
sort(a)
print(a)
