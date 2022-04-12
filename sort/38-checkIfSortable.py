# https://www.geeksforgeeks.org/check-possible-sort-array-conditional-swapping-adjacent-allowed/
'''
We are given an unsorted array of integers in the range from 0 to n-1. We are allowed to swap adjacent elements in array many number of times but only if the absolute difference between these element is 1. Check if it is possible to sort the array.If yes then print “yes” else “no”. 
Examples: 
 

Input : arr[] = {1, 0, 3, 2}
Output : yes
Explanation:- We can swap arr[0] and arr[1].
Again we swap arr[2] and arr[3]. 
Final arr[] = {0, 1, 2, 3}.

Input : arr[] = {2, 1, 0}
Output : no
'''
def isSortable(a):
    n = len(a)
    for i in range(1, n):
        if a[i] < a[i - 1]:
            if a[i-1] - a[i] == 1:
                a[i-1], a[i] = a[i], a[i-1]
            else:
                return False
    return True

a = [1, 2, 3]
print(isSortable(a))
