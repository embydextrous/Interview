'''
Given an array of digits (values are from 0 to 9), find the minimum possible sum of two numbers
formed from digits of the array. All digits of given array must be used to form the two numbers. 
Examples : 
 
Input: [6, 8, 4, 5, 2, 3]
Output: 604
The minimum sum is formed by numbers 
358 and 246

Input: [5, 3, 0, 7, 4]
Output: 82
The minimum sum is formed by numbers 
35 and 047 
'''
def minsum(a):
    a.sort()
    n1 = 0
    n2 = 0
    i = 0
    while i < len(a):
        n1 = n1 * 10 + a[i]
        i += 1
        if i == len(a):
            break
        n2 = n2 * 10 + a[i]
        i += 1
    return n1 + n2

a = [6, 8, 4, 5, 2, 3]
print(minsum(a))

