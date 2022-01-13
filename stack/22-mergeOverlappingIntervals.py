# https://www.geeksforgeeks.org/merging-intervals/

def mergeIntervals(intervals):
    intervals.sort(key = lambda x : x[0])
    s = [intervals[0]]
    for i in range(1, len(intervals)):
        if intervals[i][0] <= s[-1][1]:
            popInterval = s.pop()
            s.append([popInterval[0], max(popInterval[1], intervals[i][1])])
        else:
            s.append(intervals[i])
    return s

intervals = [[6,8], [1,3], [2,4], [5,7]]
print(mergeIntervals(intervals))
