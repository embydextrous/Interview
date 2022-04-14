'''
Given n friends, each one can remain single or can be paired up with some other friend. 
Each friend can be paired only once. Find out the total number of ways in which friends can remain single 
or can be paired up. 

Examples: 

Input  : n = 3
Output : 4
Explanation:
{1}, {2}, {3} : all single
{1}, {2, 3} : 2 and 3 paired but 1 is single.
{1, 2}, {3} : 1 and 2 are paired but 3 is single.
{1, 3}, {2} : 1 and 3 are paired but 2 is single.
Note that {1, 2} and {2, 1} are considered same.

Mathematical Explanation:
The problem is simplified version of how many ways we can divide n elements into multiple groups.
(here group size will be max of 2 elements).
In case of n = 3, we have only 2 ways to make a group: 
    1) all elements are individual(1,1,1)
    2) a pair and individual (2,1)
In case of n = 4, we have 3 ways to form a group:
    1) all elements are individual (1,1,1,1)
    2) 2 individuals and one pair (2,1,1)
    3) 2 separate pairs (2,2)

nth person can be treated in two ways:
1. Can be kept separate which is equivalent to number of ways in which n-1 persons can be paired.
2. Can be paired with anyone. So, we need to find partner which can be done in n - 1 ways. We need to multiply
    it by number of ways in which (n-2) persons can be paired now.

So, we get recurrence relation as:
P(n) = P(n-1) + (n - 1) * P(n-2)

Base cases:
P(0) = 1 -> O persons can be paired in one way.
P(1) = 1 -> 1 person can be only kept alone.
'''
def friendPairing(n):
    if n <= 1:
        return 1
    a, b = 1, 1
    for i in range(2, n + 1):
        a, b = b, b + (i - 1) * a
    return b

print(friendPairing(20000))