'''
Given an array of 0s and 1s, find the position of 0 to be replaced with 1 to get longest continuous 
sequence of 1s. Expected time complexity is O(n) and auxiliary space is O(1). 

Example: 

Input: 
   arr[] =  {1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1}
Output:
  Index 9
Assuming array index starts from 0, replacing 0 with 1 at index 9 causes
the maximum continuous sequence of 1s.

Input: 
   arr[] =  {1, 1, 1, 1, 0, 1, 1, 0, 1, 0}
Output:
  Index 4
'''
def findIndex(a):
    zeroCount = 0
    l, r = 0, 0
    bestL = bestWindow = 0
    while r < len(a):
        if zeroCount <= 1:
            if a[r] == 0:
                zeroCount += 1
            r += 1
        if zeroCount > 1:
            if a[l] == 0:
                zeroCount -= 1
            l += 1
        if zeroCount <= 1 and r-l > bestWindow:
            bestWindow = r - l
            bestL = l
    for i in range(bestL, bestL + bestWindow):
        if a[i] == 0:
            return i
    return -1

def findIndex(a):
    prevZeroIndex = prevPrevZeroIndex = -1
    maxi = 0
    resultIndex = -1
    for i in range(len(a)):
        if a[i] == 0:
            prevPrevZeroIndex, prevZeroIndex = prevZeroIndex, i
        if i - prevPrevZeroIndex > maxi:
            maxi = i - prevPrevZeroIndex
            if a[i] == 0:
                resultIndex = i
            else:
                resultIndex = prevZeroIndex
    return resultIndex

a = [1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1]
print(findIndex(a))