'''
Given an array of integers, task is to print the array in the order - largest number, smallest number, 
2nd largest number, 2nd smallest number, 3rd largest number, 3rd smallest number and so on…..
Examples: 
 
Input : arr[] = [5, 8, 1, 4, 2, 9, 3, 7, 6]
Output :arr[] = {9, 1, 8, 2, 7, 3, 4, 6, 5}

Input : arr[] = [1, 2, 3, 4]
Output :arr[] = {4, 1, 3, 2}
'''
def rearrange(a):
    a.sort()
    n = len(a)
    maxElement = n + 1
    l, r = 0, n - 1
    for i in range(n):
        if i % 2 == 0:
            a[i] += a[r] % maxElement * maxElement
            r -= 1
        else:
            a[i] += a[l] % maxElement * maxElement
            l += 1
    for i in range(n):
        a[i] = (a[i] - a[i] % maxElement) // maxElement

a = [5, 8, 1, 4, 2, 9, 3, 7, 6]
rearrange(a)
print(a)