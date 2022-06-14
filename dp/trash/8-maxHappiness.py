'''
A trip to mystical land is going to be organized in ByteLand, the city of Bytes. Unfortunately, there are limited seats say A and there are N number of groups of people. 
Every group can have old person o, child c, man m and woman w. The organizing committee wants to maximize the happiness value of the trip. Happiness value of the trip is 
the sum of the happiness value of all the groups that are going. A group will go for the trip if every member can get a seat (Breaking a group is not a good thing). 

    The happiness of child c = 4
    The happiness of woman w = 3
    The happiness of man m = 2
    The happiness of the old person o = 1

The happiness of group G, H(G) = (sum of happiness of people in it) * (number of people in the group). 
The happiness of the group ('coow') = (4 + 1 + 1 + 3) * 4 = 36.
Given the groups and the total seating capacity, the task is to maximize the happiness and print the maximized happiness of the groups going on the trip.
Examples: 

    Input: groups[] = {“mmo”, “oo”, “cmw”, “cc”, “c”}, A = 5 
    Output: 43 
    Pick these groups ['cmw', 'cc'] to get the maximum profit of (4 + 2 + 3) * 3 + (4 + 4) * 2 = 43
    Input: groups[] = {“ccc”, “oo”, “cm”, “mm”, “wwo”}, A = 10 
    Output: 77 
'''
def charToHappiness(c):
    if c == 'c':
        return 4
    if c == 'w':
        return 3
    if c == 'm':
        return 2
    return 1

def maxHappiness(groups, S):
    happiness = []
    for group in groups:
        h = 0
        for c in group:
            h += charToHappiness(c)
        happiness.append(h)
    print(happiness)
    n = len(groups)
    dp = [[0 for i in range(S+1)] for j in range(n+1)]
    for i in range(1, n+1):
        s = len(groups[i-1])
        h = happiness[i-1] * s
        for j in range(1, S+1):
            if j < s:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], h + dp[i-1][j-s])
    return dp[n][S]

groups = ["mmo", "oo", "cmw", "cc", "c"]
S = 5
print(maxHappiness(groups, S))