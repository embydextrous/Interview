'''Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent 
elements if they are in wrong order.
In each iteration max element bubbles to top. If no swaps are made in an iteration means array is sorted.
'''
# Time Complexity - O(n^2) for average and worst cases, O(n) for best case (if array is already sorted).
# Stable Sort
def bubbleSort(a):
    n = len(a)
    for i in range(n):
        swapMade = False
        for j in range(n-i-1):
            if a[j] > a[j + 1]:
                a[j], a[j+1] = a[j+1], a[j]
                swapMade = True
        if not swapMade:
            return

a = [3, 2, 7, 8, 3, 1, 9, 6, 2, 1]
bubbleSort(a)
print(a)