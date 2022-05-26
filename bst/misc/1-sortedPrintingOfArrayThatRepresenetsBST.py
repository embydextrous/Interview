# https://www.geeksforgeeks.org/sorted-order-printing-of-an-array-that-represents-a-bst/

'''
Given an array that stores a complete Binary Search Tree, write a function that efficiently 
prints the given array in ascending order. For example, given an array 
[4, 2, 5, 1, 3], the function should print 1, 2, 3, 4, 5
'''
def printArray(a, idx):
    if idx < len(a):
        printArray(a, 2 * idx + 1)
        print(a[idx], end = " ")
        printArray(a, 2 * idx + 2)

a = [4, 2, 5, 1, 3]
printArray(a, 0)
print()