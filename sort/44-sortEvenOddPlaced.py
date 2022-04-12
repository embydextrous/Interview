'''
We are given an array of n distinct numbers. The task is to sort all even-placed numbers in increasing 
and odd-placed numbers in decreasing order. The modified array should contain all sorted even-placed 
numbers followed by reverse sorted odd-placed numbers.
Note that the first element is considered as even placed because of its index 0. 

Examples:  

Input:  arr[] = {0, 1, 2, 3, 4, 5, 6, 7}
Output: arr[] = {0, 2, 4, 6, 7, 5, 3, 1}
Even-place elements : 0, 2, 4, 6
Odd-place elements : 1, 3, 5, 7
Even-place elements in increasing order : 
0, 2, 4, 6
Odd-Place elements in decreasing order : 
7, 5, 3, 1

Input: arr[] = {3, 1, 2, 4, 5, 9, 13, 14, 12}
Output: {2, 3, 5, 12, 13, 14, 9, 4, 1}
Even-place elements : 3, 2, 5, 13, 12
Odd-place elements : 1, 4, 9, 14
Even-place elements in increasing order : 
2, 3, 5, 12, 13
Odd-Place elements in decreasing order : 
14, 9, 4, 1 
'''
def sort(a):
    n = len(a)
    l = 1
    r = (n - 1) if n % 2 == 1 else n - 2
    while l < r:
        a[l], a[r] = a[r], a[l]
        l += 2
        r -= 2
    m = (n + 1) // 2
    a[:m] = sorted(a[:m])
    a[m:] = sorted(a[m:])[::-1]

a = [0, 1, 2, 3, 4, 5, 6, 7]
sort(a)
print(a)