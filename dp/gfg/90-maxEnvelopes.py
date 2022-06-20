'''
Given N number of envelopes, as {W, H} pair, where W as the width and H as the height. One envelope can fit into 
another if and only if both the width and height of one envelope is greater than the width and height of the other
envelope. Find the maximum number of envelopes that can be put inside another envelope and so on. 
Rotation of envelope is not allowed.

Examples:

    Input: envelope[] = {{4, 3}, {5, 3}, {5, 6}, {1, 2}}
    Output: 3
    Explanation: 
    The maximum number of envelopes that can be put into another envelope 
    is 3.
    ({1, 2}, {4, 3}, {5, 6})

    Input: envelope[] = {{3, 6}, {5, 4}, {4, 8}, {6, 9}, {10, 7}, {12, 12}}
    Output: 4
    Explanation:
    The maximum number of envelopes that can be put into another envelope is 4.
     ({3, 6}, {4, 8}, {6, 9}, {12, 12})
'''
def maxEnvelopes(envelopes):
    n = len(envelopes)
    envelopes.sort(key = lambda x : x[0] * x[1])
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if envelopes[i][0] > envelopes[j][0] and envelopes[i][1] > envelopes[j][1] and 1 + dp[j] > dp[i]:
                dp[i] = 1 + dp[j]
    return max(dp)

envelopes = [[3, 6], [5, 4], [4, 8], [6, 9], [10, 7], [12, 12]]
print(maxEnvelopes(envelopes))

envelopes = [[4, 3], [5, 3], [5, 6], [1, 2]]
print(maxEnvelopes(envelopes))