# https://www.geeksforgeeks.org/find-a-pair-with-the-given-difference/

'''
Given an unsorted array and a number n, find if there exists a pair of elements in the array 
whose difference is n. 
Examples: 
 

Input: arr[] = {5, 20, 3, 2, 50, 80}, n = 78
Output: Pair Found: (2, 80)

Input: arr[] = {90, 70, 20, 80, 50}, n = 45
Output: No Such Pair
'''
# Hashing solution
def findPairWithDiff(a, x):
    posDiff = abs(x)
    s = set()
    for i in a:
        if i - posDiff in s:
            return (i, i - posDiff)
        else:
            s.add(i)
    return None

# Sorting based solution
def findPairWithDiff(a, x):
    a.sort()
    i = 0
    j = 1
    while i < len(a) and j < len(a):
        if i != j and a[j] - a[i] == x:
            return (a[j], a[i])
        elif a[j] - a[i] > x:
            i += 1
        else:
            j += 1
    return None 

a = [1, 80, 88, 95]
print(findPairWithDiff(a, 15))
