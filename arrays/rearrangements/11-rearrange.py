'''
Given an array of positive and negative numbers, arrange them in an alternate fashion such that every 
positive number is followed by negative and vice-versa maintaining the order of appearance. 
Number of positive and negative numbers need not be equal. If there are more positive numbers they appear at the end of the array. If there are more negative numbers, they too appear in the end of the array.

Examples : 

Input:  arr[] = {1, 2, 3, -4, -1, 4}
Output: arr[] = {-4, 1, -1, 2, 3, 4}

Input:  arr[] = {-5, -2, 5, 2, 4, 7, 1, 8, 0, -8}
output: arr[] = {-5, 5, -2, 2, -8, 4, 7, 1, 8, 0}
'''

# Simple - If you find an element that is out of order, 
# find next element of opposite sign and right rotate by 1
# if there is none of opposite sign its done.
def rearrange(a):
    for i in range(len(a)):
        if (i % 2 == 0 and a[i] >= 0) or (i % 2 == 1 and a[i] < 0):
            l = i
            r = -1
            for j in range(l + 1, len(a)):
                if (a[l] >= 0 and a[j] < 0) or (a[l] < 0 and a[j] >= 0):
                    r = j
                    break
            if r == -1:
                break
            x = a[r]
            for i in range(r, l, -1):
                a[i] = a[i-1]
            a[l] = x


a = [-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]
rearrange(a)
print(a)

