'''
There are n people and two identical voting machines. We are also given an array a[] of size n such that a[i] stores time required by i-th person to go 
to any machine, mark his vote and come back. At one time instant, only one person can be there on each of the machines. Given a value x, defining the 
maximum allowable time for which machines are operational, check whether all persons can cast their vote or not.

Examples: 

Input  : n = 3, x = 4
         a[] = {2, 4, 2}
Output: YES
There are  n = 3 persons say and maximum
allowed time is x = 4 units. Let the persons
be P0, P1, and P2 and two machines be M0 and M1.
At t0: P0 goes to M0
At t0: P1 goes to M1
At t2: M0 is free, P2 goes to M0
At t4: both M0 and M1 are free and all 3 have
        given their vote.
'''
def canAllVoteUtil(a, W1, W2, idx, dp):
    if idx >= len(a):
        return 0
    if dp[W1][W2][idx] != -1:
        return dp[W1][W2][idx]
    fw1 = 0
    if a[idx] <= W1:
        fw1 = a[idx] + canAllVoteUtil(a, W1 - a[idx], W2, idx + 1, dp)
    fw2 = 0
    if a[idx] <= W2:
        fw2 = a[idx] + canAllVoteUtil(a, W1, W2 - a[idx], idx + 1, dp)
    dp[W1][W2][idx] = max(canAllVoteUtil(a, W1, W2, idx + 1, dp), fw1, fw2)
    return dp[W1][W2][idx]

def canAllVote(a, X):
    s = sum(a)
    n = len(a)
    dp = [[[-1 for i in range(n)] for j in range(X+1)] for k in range(X+1)]
    canAllVoteUtil(a, X, X, 0, dp)
    print(dp[X][X][0])
    return dp[X][X][0] == s

X = 4
a = [2, 4, 2]
print(canAllVote(a, X))
