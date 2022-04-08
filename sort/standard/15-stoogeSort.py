# https://www.geeksforgeeks.org/stooge-sort/
'''
The Stooge sort is a recursive sorting algorithm. It is defined as below (for ascending order sorting).  

Step 1 : If value at index 0 is greater than
         value at last index, swap them.
Step 2:  Recursively, 
       a) Stooge sort the initial 2/3rd of the array.
       b) Stooge sort the last 2/3rd of the array.
       c) Stooge sort the initial 2/3rd again to confirm.
'''
'''
The running time complexity of stooge sort can be written as, T(n) = 3T(3n/2) + O(1)
Solution of above recurrence is O(n(log3/log1.5)) = O(n^2.709), hence it is slower than even bubble sort(n^2). 
'''
def stoogesort(arr, l, r):
    if l >= r:
        return
    if arr[l] > arr[r]:
        arr[l], arr[r] = arr[r], arr[l]
  
    if r - l + 1 > 2:
        t = (r- l + 1) // 3
        stoogesort(arr, l, r - t)
        stoogesort(arr, l + t, r)
        stoogesort(arr, l, r - t)

a = [3, 5, 1, 7, 9, 2, 4, 8, 6]
stoogesort(a, 0, len(a) - 1)
print(a)