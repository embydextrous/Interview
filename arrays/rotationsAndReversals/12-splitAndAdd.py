# Same as left rotate except we don't take mod now in case k > length of array
'''
There is a given array and split it from a specified position, and move the first part of the array add to the end. 
 

Split the array and add the first part to the end

Examples: 
 

Input : arr[] = {12, 10, 5, 6, 52, 36}
            k = 2
Output : arr[] = {5, 6, 52, 36, 12, 10}
Explanation : Split from index 2 and first 
part {12, 10} add to the end .

Input : arr[] = {3, 1, 2}
           k = 1
Output : arr[] = {1, 2, 3}
Explanation : Split from index 1 and first
part add to the end.
'''
def reverse(a, l, r):
    while l < r:
        a[l], a[r] = a[r], a[l]
        l += 1
        r -= 1

def splitAndAdd(a, k):
    n = len(a)
    if k >= n - 1:
        return
    reverse(a, 0, k-1)
    reverse(a, k, n-1)
    reverse(a, 0, n-1)

a = [1, 2, 3, 4, 5, 6, 7]
splitAndAdd(a, 2)
print(a)