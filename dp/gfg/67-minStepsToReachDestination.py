'''
Given a number line from -infinity to +infinity. You start at 0 and can go either to the left or to the right. The condition is that in i'th move, 
you take i steps. 
a) Find if you can reach a given number x 
b) Find the most optimal way to reach a given number x, if we can indeed reach it. For example, 3 can be reached in 2 steps, (0, 1) (1, 3) 
and 4 can be reached in 3 steps (0, -1), (-1, 1) (1, 4).
'''
from collections import deque

def minSteps(N):
    # symmetry
    N = abs(N)
    step = sum = 0
    # Why check for even because it will be subtracted twice.
    while sum < N or (sum - N) % 2 == 1:
        step += 1
        sum += step
    return step

        