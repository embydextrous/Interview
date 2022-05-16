# https://www.geeksforgeeks.org/maximum-difference-group-k-elements-rest-array/
'''
You are given an array of n elements. You have to divide the given array into two group such that one group
consists exactly k elements and second group consists rest of elements. Your result must be maximum possible
difference of sum of elements of these two group.
Examples: 
 

Input : arr[n] = {1, 5, 2, 6, 3}  , k = 2
Output : Maximum Difference = 11
Explanation : group1 = 1+2 , group2 = 3+5+6
              Maximum Difference = 14 - 3 = 11

Input : arr[n] = {1, -1, 3, -2, -3} , k = 2
Output : Maximum Difference = 10
Explanation : group1 = -1-2-3 , group2 = 1+3
              Maximum Difference = 4 - (-6) = 10
'''
import heapq

def minDiff(a, k):
    arrSum = sum(a)
    kSmallestSum = sum(heapq.nsmallest(k, a))
    kLargestSum = sum(heapq.nlargest(k, a))
    return max(abs(arrSum - 2 * kSmallestSum), abs(arrSum - 2 * kLargestSum))

a = [1, -1, 3, -2, -3]
print(minDiff(a, 2))

# g1 - s + g1
# g2 = s - g1