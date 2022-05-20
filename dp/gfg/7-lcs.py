'''
Given two sequences, find the length of longest subsequence present in both of them.

For ex:

Input
AGGTAB
GXTXAYB

Output
GTAB

x       A   G   G   T   A   B
    0   0   0   0   0   0   0
G   0   0   1   1   1   1   1
X   0   0   1   1   1   1   1
T   0   0   1   1   2   2   2
X   0   0   1   1   2   2   2
A   0   1   1   1   2   3   3
Y   0   1   1   1   2   3   3
B   0   1   1   1   2   3   4
'''
from collections import deque


def lcs(s1, s2):
    n, m = len(s1), len(s2)
    M = [[0 for i in range(m+1)] for j in range(2)]
    for c in s1:
        for i in range(1, m + 1):
            if c == s2[i-1]:
                M[1][i] = M[0][i-1] + 1
            else:
                M[1][i] = max(M[0][i], M[1][i-1])
        M[0] = M[1]
    return M[1][m]

def constructLcs(s1, s2):
    n, m = len(s1), len(s2)
    M = [[0 for i in range(m+1)] for j in range(n+1)]
    for i in range(n+1):
        c = s1[i-1]
        for j in range(1, m + 1):
            if c == s2[j-1]:
                M[i][j] = M[i-1][j-1] + 1
            else:
                M[i][j] = max(M[i-1][j], M[i][j-1])
    i = n
    j = m
    lcs = deque()
    while i > 0 and j > 0:
        if s1[i-1] == s2[j-1]:
            lcs.appendleft(s1[i-1])
            i -= 1
            j -= 1
        elif M[i][j-1] > M[i-1][j]:
            j -= 1
        else:
            i -= 1
    return "".join(lcs)
    

s2 = "AGGTAB"
s1 = "GXTXYAB"
print(lcs(s2, s1))
print(constructLcs(s2, s1))