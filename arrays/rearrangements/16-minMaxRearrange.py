'''
Given an array of integers, task is to print the array in the order - largest number, smallest number, 
2nd largest number, 2nd smallest number, 3rd largest number, 3rd smallest number and so on…..
Examples: 
 

Input : arr[] = [5, 8, 1, 4, 2, 9, 3, 7, 6]
Output :arr[] = {9, 1, 8, 2, 7, 3, 4, 6, 5}

Input : arr[] = [1, 2, 3, 4]
Output :arr[] = {1, 4, 2, 3}
'''
def rearrange(a):
    a.sort()
    result = [0 for i in range(len(a))]
    l, r = 0, len(a) - 1
    for i in range(len(a)):
        if i % 2 == 0:
            result[i] = a[r]
            r -= 1
        else:
            result[i] = a[l]
            l += 1
    for i in range(len(a)):
        a[i] = result[i]
    
a = [5, 8, 1, 4, 2, 9, 3, 7, 6]
rearrange(a)
print(a)

