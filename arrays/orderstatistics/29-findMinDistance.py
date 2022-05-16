import sys

'''
Given an unsorted array arr[] and two numbers x and y, find the minimum distance between x and y in arr[]. 
The array might also contain duplicates. You may assume that both x and y are different and present in arr[].

Examples: 

Input: arr[] = {1, 2}, x = 1, y = 2
Output: Minimum distance between 1 
and 2 is 1.
Explanation: 1 is at index 0 and 2 is at 
index 1, so the distance is 1

Input: arr[] = {3, 4, 5}, x = 3, y = 5
Output: Minimum distance between 3 
and 5 is 2.
Explanation:3 is at index 0 and 5 is at 
index 2, so the distance is 2

Input: 
arr[] = {3, 5, 4, 2, 6, 5, 6, 6, 5, 4, 8, 3},  
x = 3, y = 6
Output: Minimum distance between 3 
and 6 is 4.
Explanation:3 is at index 0 and 6 is at 
index 5, so the distance is 4

Input: arr[] = {2, 5, 3, 5, 4, 4, 2, 3}, 
x = 3, y = 2
Output: Minimum distance between 3 
and 2 is 1.
Explanation:3 is at index 7 and 2 is at 
index 6, so the distance is 1
'''

def findMinDistance(a, x, y):
    i = j = -1
    valueToLookFor = None
    minDist = len(a)
    for k in range(len(a)):
        if a[k] == x:
            if valueToLookFor == x:
                minDist = min(minDist, k - j)
            valueToLookFor = y
            i = k
        elif a[k] == y:
            if valueToLookFor == y:
                minDist = min(minDist, k - i)
            valueToLookFor = x
            j = k
    return minDist

a = [3, 5, 4, 2, 6, 5, 6, 6, 5, 4, 8, 3]
x = 3
y = 1
print(findMinDistance(a, x, y))



