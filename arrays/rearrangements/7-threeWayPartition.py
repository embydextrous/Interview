'''
Given an array and a range [lowVal, highVal], partition the array around the range such that array 
is divided in three parts. 
1) All elements smaller than lowVal come first. 
2) All elements in range lowVal to highVVal come next. 
3) All elements greater than highVVal appear in the end. 
The individual elements of three sets can appear in any order.

Examples: 

Input: arr[] = {1, 14, 5, 20, 4, 2, 54, 20, 87, 98, 3, 1, 32}  
        lowVal = 14, highVal = 20
Output: arr[] = {1, 5, 4, 2, 1, 3, 14, 20, 20, 98, 87, 32, 54}

Input: arr[] = {1, 14, 5, 20, 4, 2, 54, 20, 87, 98, 3, 1, 32}  
       lowVal = 20, highVal = 20       
Output: arr[] = {1, 14, 5, 4, 2, 1, 3, 20, 20, 98, 87, 32, 54} 
'''
def threeWayPartition(a, low, high):
    l = m = 0
    r = len(a) - 1
    while m <= r:
        if a[m] < low:
            a[m], a[l] = a[l], a[m]
            m += 1
            l += 1
        elif a[m] <= high:
            m += 1
        else:
            a[m], a[r] = a[r], a[m]
            r -= 1

a = [1, 14, 5, 20, 4, 2, 54, 20, 87, 98, 3, 1, 32]
low = 14
high = 20
threeWayPartition(a, low, high)
print(a)

#   1, 14, 5, 1, 4, 2, 3r, 87lm, 98, 20, 54, 32, 20