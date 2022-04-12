'''
Given an array of positive and negative numbers, arrange them such that all negative integers appear before 
all the positive integers in the array without using any additional data structure like hash table, arrays, etc. 
The order of appearance should be maintained.

Examples:  

Input:  [12 11 -13 -5 6 -7 5 -3 -6]
Output: [-13 -5 -7 -3 -6 12 11 6 5]

Recomme
'''
def rearrange(a, l, r):
    if l < r:
        m = l + (r - l) // 2
        rearrange(a, l, m)
        rearrange(a, m + 1, r)
        merge(a, l, m, r)

def merge(a, l, m, r):
    i = l
    j = m + 1
    # a[i:m+1] is positive
    while i <= m and a[i] < 0:
        i += 1
    # a[m+1:j] is negative
    while j <= r and a[j] < 0:
        j += 1
    # reverse positive part of left array
    reverse(a, i, m)
    # reverse negative part of right array
    reverse(a, m + 1, j - 1)
    # reverse between i and j
    reverse(a, i, j - 1)

def reverse(a, l, r):
    while l < r:
        a[l], a[r] = a[r], a[l]
        l += 1
        r -= 1

a = [12, 11, -13, -5, 6, -7, 5, -3, -6]
rearrange(a, 0, len(a) - 1)
print(a)