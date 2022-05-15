'''
An array contains both positive and negative numbers in random order. Rearrange the array elements so 
that positive and negative numbers are placed alternatively. Number of positive and negative numbers 
need not be equal. If there are more positive numbers they appear at the end of the array. If there 
are more negative numbers, they too appear in the end of the array.
For example, if the input array is [-1, 2, -3, 4, 5, 6, -7, 8, 9], then the output should be 
[9, -7, 8, -3, 5, -1, 2, 4, 6]

9 -7 2 -3 8 -1 4 5 6 -1
'''
def rearrange(a):
    l = 0
    r = len(a) - 1
    for i in range(l, r):
        if a[i] < 0:
            a[i], a[l] = a[l], a[i]
            l += 1
    if a[r] < 0:
        a[r], a[l] = a[l], a[r]
    print(a)
    i = 0
    j = l
    while a[i] < 0:
        a[i], a[j] = a[j], a[i]
        j += 1
        i += 2
    print(a)

# -1, -3, -7, 4, 5, 2, 8, 9
a = [-1, 2, -3, 4, 5, 6, -7, 8, 9]
rearrange(a)