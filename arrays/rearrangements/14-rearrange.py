'''
Given two integer arrays of same size, “arr[]” and “index[]”, reorder elements in “arr[]” according 
to given index array. It is not allowed to given array arr's length.

Example: 

Input:  arr[]   = [10, 11, 12];
        index[] = [1, 0, 2];
Output: arr[]   = [11, 10, 12]
        index[] = [0,  1,  2] 

Input:  arr[]   = [50, 40, 70, 60, 90]
        index[] = [3,  0,  4,  1,  2]
Output: arr[]   = [40, 60, 90, 50, 70]
        index[] = [0,  1,  2,  3,   4]
'''
def rearrange(a, index):
    n = len(a)
    for i in range(n):
        while index[i] != i:
            a[i], a[index[i]] = a[index[i]], a[i]
            index[index[i]], index[i] = index[i], index[index[i]]

a = [50, 40, 70, 60, 90]
index = [3, 0, 4, 1, 2]
rearrange(a, index)
print(a)
print(index)