'''
For a given array of n integers and assume that '0' is an invalid number and all others as a valid number. 
Convert the array in such a way that if both current and next element is valid and both have same value 
then double current value and replace the next number with 0. After the modification, rearrange the array
 such that all 0's shifted to the end. 
Examples: 

Input : arr[] = {2, 2, 0, 4, 0, 8}
Output : 4 4 8 0 0 0

Input : arr[] = {0, 2, 2, 2, 0, 6, 6, 0, 0, 8}
Output :  4 2 12 8 0 0 0 0 0 0
'''
def transform(a):
    n = len(a)
    i = 0
    while i < n:
        if a[i] == 0:
            i += 1
        else:
            if i != 0 and a[i-1] == a[i]:
                a[i-1] *= 2
                a[i] = 0
            i += 1
    for i in range(n):
        if a[i] == 0:
            l = i
            r = -1
            for j in range(l + 1, n):
                if a[j] != 0:
                    r = j
                    break
            if r == -1:
                break
            x = a[r]
            for j in range(r, l, -1):
                a[j] = a[j-1]
            a[l] = x

a = [0, 2, 2, 2, 0, 6, 6, 0, 0, 8]
transform(a)
print(a)