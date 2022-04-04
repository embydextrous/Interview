# https://www.geeksforgeeks.org/binary-search-for-rational-numbers-without-using-floating-point-arithmetic/

'''
A rational is represented as p/qb, for example 2/3. Given a sorted array of rational numbers, 
how to search an element using Binary Search. Use of floating-point arithmetic is not allowed.

Example:  

Input:  arr[] = {1/5, 2/3, 3/2, 13/2}
        x = 3/2
Output: Found at index 2
'''
def search(a, l, r, x):
    if l > r:
        return -1
    m = l + (r - l) // 2
    lhs = a[m][0] * x[1]
    rhs = a[m][1] * x[0]
    if lhs == rhs:
        return m
    if lhs > rhs:
        return search(a, l, m - 1, x)
    return search(a, m + 1, r, x)

a = [[1, 5], [2, 3], [3, 2], [13, 2]]
x = [3, 2]
print(search(a, 0, len(a)- 1, x))