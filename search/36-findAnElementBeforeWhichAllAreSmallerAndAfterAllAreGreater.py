# https://www.geeksforgeeks.org/find-the-element-before-which-all-the-elements-are-smaller-than-it-and-after-which-all-are-greater-than-it/

'''
Given an array, find an element before which all elements are smaller than it, and after which all are greater than it.
Return the index of the element if there is such an element, otherwise, return -1.

Examples:

    Input: arr[] = {5, 1, 4, 3, 6, 8, 10, 7, 9}; 
    Output: 4 
    Explanation: All elements on left of arr[4] are smaller than it 
    and all elements on right are greater.

    Input: arr[] = {5, 1, 4, 4}; 
    Output: -1 
'''
def search(a):
    n = len(a)
    leftMax = a[:]
    rightMin = a[:]
    for i in range(1, n):
        leftMax[i] = max(leftMax[i], leftMax[i-1])
    for i in range(n-2, -1, -1):
        rightMin[i] = min(rightMin[i], rightMin[i+1])
    for i in range(n):
        if leftMax[i] == a[i] and rightMin[i] == a[i]:
            return a[i]
    print(leftMax)
    print(rightMin)
    return None
            
a = [5, 1, 4, 3, 6, 8, 10, 7, 9]
print(search(a))