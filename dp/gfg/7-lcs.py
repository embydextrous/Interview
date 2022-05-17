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
def lcs(s1, s2):
    n, m = len(s1), len(s2)
    M = [[0 for i in range(m+1)] for j in range(2)]
    for c in s1:
        for i in range(1, m + 1):
            if c == s2[i-1]:
                M[1][i] = M[0][i-1] + 1
            else:
                M[1][i] = max(M[0][i], M[1][i-1])
        print(M[1])
        M[0], M[1] = M[1], M[0]
    print(M)
    return M[0][m]

s2 = "AGGTAB"
s1 = "GXTXYAB"
print(lcs(s1, s2))