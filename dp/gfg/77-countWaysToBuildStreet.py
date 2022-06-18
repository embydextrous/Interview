'''
There is a street of length n and as we know it has two sides. Therefore a total of 2 * n spots are available. In each of these spots either a house or an office can be built with following 2 restrictions: 

1. No two offices on the same side of the street can be adjacent. 
2. No two offices on different sides of the street can be exactly opposite to each other i.e. they can't overlook each other. 
There are no restrictions on building houses and each spot must either have a house or office. 
Given length of the street n, find total number of ways to build the street.

Examples:  

Input : 2
Output : 7
Please see below diagram for explanation.

Input : 3
Output : 17
'''
def countWays(n):
    if n == 0:
        return 0
    a, b = 1, 0
    for i in range(1, n + 1):
        a, b = (a + b), b + 2 * a
    return a + b
    
n = 5
print(countWays(5))

