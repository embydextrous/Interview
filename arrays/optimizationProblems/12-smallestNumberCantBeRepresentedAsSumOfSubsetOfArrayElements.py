# https://www.geeksforgeeks.org/find-smallest-value-represented-sum-subset-given-array/

'''
Given a sorted array (sorted in non-decreasing order) of positive numbers, 
find the smallest positive integer value that cannot be represented as the sum of elements of any subset 
of a given set. 
Examples: 
 
Input:  arr[] = {1, 3, 6, 10, 11, 15};
Output: 2

Input:  arr[] = {1, 1, 1, 1};
Output: 5

Input:  arr[] = {1, 1, 3, 4};
Output: 10

Input:  arr[] = {1, 2, 5, 10, 20, 40};
Output: 4

Input:  arr[] = {1, 2, 3, 4, 5, 6};
Output: 22
'''

# Simple Logic 
# Let say answer is 1
# If answer is smaller than array element, it is the answer.
# Else, we can represenet elements till result - 1 with left side elements and hence we can represent 
# result - 1 + current element too. So, next candidate is result + current element.

def findMin(a):
    result = 1
    for i in a:
        if i > result:
            break
        result += i
    return result

a = [1, 3, 6, 10, 11, 15]
print(findMin(a))