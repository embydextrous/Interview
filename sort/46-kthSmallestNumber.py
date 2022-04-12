# https://www.geeksforgeeks.org/k-th-smallest-element-removing-integers-natural-numbers/
'''
Given an array arr[] of size 'n' and a positive integer k. Consider series of natural numbers and 
remove arr[0], arr[1], arr[2], …, arr[p] from it. Now the task is to find k-th smallest number in 
the remaining set of natural numbers. If no such number exists print “-1”.

Examples :  

Input : arr[] = { 1 } and k = 1.
Output: 2
Natural numbers are {1, 2, 3, 4, .... }
After removing {1}, we get {2, 3, 4, ...}.
Now, K-th smallest element = 2.

Input : arr[] = {1, 3}, k = 4.
Output : 6
First 5 Natural number {1, 2, 3, 4, 5, 6,  .. }
After removing {1, 3}, we get {2, 4, 5, 6, ... }.
'''
# candidate = 5
# a[i] = 1
# k -> 0
def kthNumber(a, k):
    candidate = 1
    for i in range(len(a)):
        if a[i] - candidate < k:
            k -=  a[i] - candidate
            candidate = a[i] + 1
        else:
            return candidate + k - 1
    if k > 0:
        return candidate + k - 1

a = [1, 3, 4, 7]
print(kthNumber(a, 4))
