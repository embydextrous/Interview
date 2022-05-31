#https://www.geeksforgeeks.org/trapping-rain-water/
'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it is able to trap after raining.

Examples:  

Input: arr[]   = {2, 0, 2}
Output: 2
Explanation:
The structure is like below

XWX
XWX

We can trap 2 units of water in the middle gap.

Input: arr[]   = {3, 0, 2, 0, 4}
Output: 7
Explanation:
Structure is like below

    X
XWWWX
XWXWX
XWXWX

We can trap "3 units" of water between 3 and 2,
"1 unit" on top of bar 2 and "3 units" between 2 
and 4.  See below diagram also.

Input: arr[] = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
Output: 6

'''
# [0, 1, 0, 2, 1, 0, 1, 3r, 2l, 1, 2, 1]
lMax = 3
rMax = 2
w = 6
'''

Explanation:
The structure is like below

       X
   XWWWXXWX
 XWXXWXXXXXX 

Trap "1 unit" between first 1 and 2, "4 units" between
first 2 and 3 and "1 unit" between second last 1 and last 2
'''

# set left = 0, right = n - 1, n being length of array
# set leftMax = 0, rightMax = 0, leftMax indicates largest value till l, rightMax indicates largest value after r
# for each bar you need to find value of min(leftMax, rightMax) - barHeight to get trapped water
# if leftMax >= rightMax, min(leftMax, rightMax) will be equal to rightMax
# if rightMax > leftMax, min(leftMax, rightMax) will be equal to leftMax
def trappedWater(a):
    left = 0
    right = len(a) - 1
    leftMax = rightMax = result = 0
    while left <= right:
        if leftMax <= rightMax:
            result += max(0, leftMax - a[left])
            leftMax = max(leftMax, a[left])
            left += 1
        else:
            result += max(0, rightMax - a[right])
            rightMax = max(rightMax, a[right])
            right -= 1
    return result

a = [3, 0, 4, 0, 2]
print(trappedWater(a))