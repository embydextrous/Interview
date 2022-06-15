'''
Given a number n, find a number of ways we can add 3 non-negative integers so that their sum is n.
Examples : 
 

Input : n = 1
Output : 3
There are four ways to get sum 1.
(1, 0, 0), (0, 1, 0) and (0, 0, 1)

Input : n = 2
Output : 6
There are six ways to get sum 2.
(2, 0, 0), (0, 2, 0), (0, 0, 2), (1, 1, 0)
(1, 0, 1) and (0, 1, 1)

Input : n = 3
Output : 10
There are ten ways to get sum 10.
(3, 0, 0), (0, 3, 0), (0, 0, 3), (1, 2, 0)
(1, 0, 2), (0, 1, 2), (2, 1, 0), (2, 0, 1),
(0, 2, 1) and (1, 1, 1)
'''
# a1 + a2 + a3 .... + ak = n (where ai >= 0), number of solutions comes to be C(n + k - 1, k - 1). Here k = 3, so it is C(n + 2, 2) = ((n + 1) * (n + 2)) / 2
def numSolutions(N):
    return ((N+1) * (N+2)) // 2

n = 3
print(numSolutions(n))