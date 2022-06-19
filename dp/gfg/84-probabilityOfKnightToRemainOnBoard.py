'''
Given an NxN chessboard and a Knight at position (x,y). The Knight has to take exactly K steps, 
where at each step it chooses any of the 8 directions uniformly at random. What is the probability 
that the Knight remains in the chessboard after taking K steps, with the condition that it can't 
enter the board again once it leaves it?
Examples: 

Let's take:
8x8 chessboard,
initial position of the knight : (0, 0),
number of steps : 1
At each step, the Knight has 8 different positions to choose from. 

If it starts from (0, 0), after taking one step it will lie inside the
board only at 2 out of 8 positions, and will lie outside at other positions.
So, the probability is 2/8 = 0.25
'''
ROW = [1, -1, -2, -2, -1, 1, 2, 2]
COL = [-2, -2, -1, 1, 2, 2, 1, -1]

def probability(N, x, y, k, memo):
    if x < 0 or y < 0 or x >= N or y >= N:
        return 0
    if k == 0:
        return 1
    if (x, y, k) in memo:
        return memo[(x, y, k)]
    result = 0
    for q in range(8):
        i, j = x + ROW[q], y + COL[q]
        result += 0.125 * probability(N, i, j, k - 1, memo)
    memo[(x, y, k)] = result
    return result

N = 8
x = 0
y = 0
k = 1
memo = {}
p = probability(N, x, y, k, memo)
print(memo[(x, y, k)])
