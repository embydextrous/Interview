'''
Given an array of positive and negative numbers, arrange them such that all negative integers appear before 
all the positive integers in the array without using any additional data structure like hash table, arrays, etc. 
The order of appearance should be maintained.

Examples:  

Input:  [12 11 -13 -5 6 -7 5 -3 -6]
Output: [-13 -5 -7 -3 -6 12 11 6 5]
'''
def rearrange(a):
    n = len(a)
    l = 0
    for i in range(n):
        if a[i] < 0:
            x = a[i]
            for j in range(i, l, -1):
                a[j] = a[j-1]
            a[l] = x
            l += 1

a = [12, 11, -13, -5, 6, -7, 5, -3, -6]
rearrange(a)
print(a)