# https://www.geeksforgeeks.org/minimize-the-maximum-difference-between-the-heights/

'''
For any given tower, you have two choices, you can either increase its height or decrease it.

Now if you decide to increase its height from say Hi to Hi + K, then you can also increase the height of 
all shorter towers as that won't affect the maximum. Similarly, if you decide to decrease the height of a tower 
from Hi to Hi - K, then you can also decrease the heights of all taller towers.

We will make use of this, we have n buildings, and we'll try to make each of the building the highest 
and see making which building the highest gives us the least range of heights(which is our answer).
Let me explain:

So what we want to do is -
1) We first sort the array(you will soon see why).

2) Then for every building from i = 0 to n-2, we try make it the highest (by adding K to the building, 
adding K to the buildings on its left and subtracting K from the buildings on its right).

So say we're at building Hi, we've added K to it and the buildings before it and subtracted K from the 
buildings after it.

So the minimum height of the buildings will now be min(H0 + K, Hi+1 - K),
i.e. min(1st building + K, next building on right - K).

(Note: This is because we sorted the array. Convince yourself by taking a few examples.)

Likewise, the maximum height of the buildings will be max(Hi + K, Hn-1 - K),
i.e. max(current building + K, last building on right - K).

3) max - min gives you the range.

[1]Note that when i = n-1. In this case, there is no building after the current building, so we're adding K to every building, so the range will merely be height[n-1] - height[0] since K is added to everything, so it cancels out.
'''
import sys

def findMinDiff(a, k):
    n = len(a)
    # Sort the array
    a.sort()
    minDiff = sys.maxsize
    for i in range(n-1): # For last element k adds to each element having no effect on range
        h0 = a[0] + k
        hi = a[i] + k
        hnexti = a[i+1] - k
        hlast = a[n-1] - k
        maxHeight = max(hi, hlast)
        minHeight = min(h0, hnexti)
        minDiff = min(minDiff, maxHeight - minHeight)
    return minDiff
        
a = [1, 10, 14, 14, 14, 15]
k = 6
print(findMinDiff(a, k))
