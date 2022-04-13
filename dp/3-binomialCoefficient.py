'''
The following are the common definitions of Binomial Coefficients. 

A binomial coefficient C(n, k) can be defined as the coefficient of x^k in the expansion of (1 + x)^n.
A binomial coefficient C(n, k) also gives the number of ways, disregarding order, that k objects can be 
chosen from among n objects more formally, the number of k-element subsets (or k-combinations) of a n-element set.

The Problem 
Write a function that takes two parameters n and k and returns the value of Binomial Coefficient C(n, k). 
For example, your function should return 6 for n = 4 and k = 2, and it should return 10 for n = 5 and k = 2.
Recommended: Please solve it on “PRACTICE” first, before moving on to the solution.
'''
# Also see, https://www.geeksforgeeks.org/permutation-coefficient/
def bc(n, r):
    r = min(r, n - r)
    result = 1
    for i in range(1, r + 1):
        result *= (n - i + 1)
        result //= i
    return result

print(bc(2022, 31))
