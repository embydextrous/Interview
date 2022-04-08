'''
Cocktail Sort is a variation of Bubble sort. The Bubble sort algorithm always traverses elements from 
left and moves the largest element to its correct position in first iteration and second largest in 
second iteration and so on. Cocktail Sort traverses through a given array in both directions alternatively. 

Algorithm: 
Each iteration of the algorithm is broken up into 2 stages: 

1. The first stage loops through the array from left to right, just like the Bubble Sort. 
    During the loop, adjacent items are compared and if value on the left is greater than the value 
    on the right, then values are swapped. At the end of first iteration, largest number will reside 
    at the end of the array.
2. The second stage loops through the array in opposite direction- starting from the item just before 
    the most recently sorted item, and moving back to the start of the array. Here also, adjacent items 
    are compared and are swapped if required.
'''
'''
Worst and Average Case Time Complexity: O(n^2). 
Best Case Time Complexity: O(n). Best case occurs when array is already sorted.
Auxiliary Space: O(1)
Sorting In Place: Yes
Stable: Yes

Performs better than BubbleSort
'''
from random import randint

def cocktailSort(a):
    n = len(a)
    start = 0
    end = n - 1
    swapped = True
    while swapped:
        swapped = False
        for i in range(start, end):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                swapped = True
        if swapped == False:
            return
        swapped = False
        end -= 1
        for i in range(end, start, -1):
            if a[i-1] > a[i]:
                a[i], a[i-1] = a[i-1], a[i]
                swapped = True

a = [randint(1, 20) for i in range(20)]
cocktailSort(a)
print(a)