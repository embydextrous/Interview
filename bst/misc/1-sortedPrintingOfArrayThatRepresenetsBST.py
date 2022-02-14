# https://www.geeksforgeeks.org/sorted-order-printing-of-an-array-that-represents-a-bst/

'''
Given an array that stores a complete Binary Search Tree, write a function that efficiently 
prints the given array in ascending order. For example, given an array 
[4, 2, 5, 1, 3], the function should print 1, 2, 3, 4, 5
'''
def printArray(a, start, end):
    if start <= end:
        printArray(a, 2 * start + 1, end)
        print(a[start], end = " ")
        printArray(a, 2 * start + 2, end)

a = [4, 2, 5, 1, 3]
printArray(a, 0, len(a) - 1)
print()