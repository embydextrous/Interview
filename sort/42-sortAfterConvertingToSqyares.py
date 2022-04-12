'''
Given an array of both positive and negative integers 'arr[]' which are sorted. The task is to sort the 
square of the numbers of the Array. 
Examples: 

Input  : arr[] =  {-6, -3, -1, 2, 4, 5}
Output : 1, 4, 9, 16, 25, 36 

Input  : arr[] = {-5, -4, -2, 0, 1}
Output : 0, 1, 4, 16, 25
'''
def sort(a):
    n = len(a)
    result = [0] * n
    l = 0
    r = n - 1
    k = n - 1
    while l <= r:
        if abs(a[l]) >= abs(a[r]):
            result[k] = a[l] * a[l]
            l += 1
        else:
            result[k] = a[r] * a[r]
            r -= 1
        k -= 1
    a[:] = result[:]

a = [-6, -3, -1, 2, 4, 5]
sort(a)
print(a)