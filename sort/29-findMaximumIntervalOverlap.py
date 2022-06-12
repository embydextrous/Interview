'''
Consider a big party where a log register for guest's entry and exit times is maintained. Find the time at which there 
are maximum guests in the party. Note that entries in register are not in any order.
Example : 

Input: arrl[] = {1, 2, 9, 5, 5}
       exit[] = {4, 5, 12, 9, 12}

# 1 2 5 5 9
# 4 5 9 12 9
First guest in array arrives at 1 and leaves at 4, 
second guest arrives at 2 and leaves at 5, and so on.

Output: 5
There are maximum 3 guests at time 5.  
'''

def maxOverlaps(intervals):
    intervals.sort(key = lambda x : (x[0], x[1]))
    n = len(intervals)
    i = 1
    j = 0
    maxOverlap = 1
    cm = 1
    while i < n and j < n:
        if intervals[i][0] <= intervals[j][1]:
            i += 1
            cm += 1
            maxOverlap = max(cm, maxOverlap)
        else:
            j += 1
            cm -= 1
    return maxOverlap

# 1 2 5 5 9
# 4 5 9 12 12
intervals = [[5, 9], [2, 5], [5, 12], [9, 12], [1, 4]]
print(maxOverlaps(intervals))