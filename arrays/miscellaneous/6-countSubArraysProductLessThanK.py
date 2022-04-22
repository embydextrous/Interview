'''
Given an array of positive numbers, calculate the number of possible contiguous subarrays having product
lesser than a given number K.

Examples : 

Input : arr[] = [1, 2, 3, 4] 
        K = 10
Output : 7
The subarrays are {1}, {2}, {3}, {4}
{1, 2}, {1, 2, 3} and {2, 3}

Input  : arr[] = [1, 9, 2, 8, 6, 4, 3] 
         K = 100
Output : 16

Input  : arr[] = [10, 5, 2, 6] 
         K = 100
Output : 8
'''
def countSubArrays(a, k):
    n = len(a)
    if n == 0:
        return 0
    i, j = 0, 0
    count = 0
    p = a[0]
    while i < n and j < n:
        if p < k:
            count += (j - i) + 1
            j += 1
            if j < n:
                p *= a[j]
        elif p >= k:
            p //= a[i]
            i += 1
    return count

a = [10, 5, 2, 6]
print(countSubArrays(a, 100))