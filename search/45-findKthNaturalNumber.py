# https://www.geeksforgeeks.org/k-th-missing-element-in-sorted-array/
'''
Given an increasing sequence a[], we need to find the K-th missing contiguous element in the increasing 
sequence which is not present in the sequence. If no k-th missing element is there output -1. 

Examples : 

Input : a[] = {2, 3, 5, 9, 10};   
        k = 1;
Output : 1
Explanation: Missing Element in the increasing 
sequence are {1,4, 6, 7, 8}. So k-th missing element
is 1

Input : a[] = {2, 3, 5, 9, 10, 11, 12};       
        k = 4;
Output : 7
Explanation: missing element in the increasing 
sequence are {1, 4, 6, 7, 8}  so k-th missing 
element is 7
'''
def findKthMissing(a, k):
    next = 1
    for i in a:
        if k - (i - next) <= 0:
            return next + k - 1
        k -= i - next
        next = i + 1
    return -1
# k - -4
# next - 12
# i - 19
a = [2,3,4,7,11]
k = 1
print(findKthMissing(a, k))