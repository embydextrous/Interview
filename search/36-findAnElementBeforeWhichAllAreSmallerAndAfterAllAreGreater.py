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
    if n <= 2:
        return -1
    idx = -1
    element = a[0]
    maxi = a[0]
    i = 1
    while i < n - 1:
        if a[i] < maxi:
            i += 1
        else:
            element = a[i]
            idx = i
            maxi = a[i]
            i += 1
            while i < n - 1:
                if a[i] >= element:
                    if a[i] > maxi:
                        maxi = a[i]
                    if i == n - 1:
                        return idx if element <= a[n-1] else -1
                    i += 1
                else:
                    i += 1
                    element = a[i]
                    idx = -1
    return idx if element <= a[n-1] else -1

a = [5, 1, 4, 3, 6, 0]
print(search(a))