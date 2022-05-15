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
    n = len(a)
    prevZeroIndex = -1
    prevPrevZeroIndex = -1
    maxi = 0
    maxIndex = -1
    for i in range(n):
        if prevZeroIndex == -1:
            maxi = i + 1
            if a[i] == 0:
                maxIndex = i
        elif prevPrevZeroIndex == -1:
            if a[i] == 0:
                if i - prevZeroIndex > maxi:
                    maxi = i - prevZeroIndex
                    maxIndex = i
            else:
                maxi = i + 1
                maxIndex = prevZeroIndex
        else:
            if a[i] == 0:
                if i - prevZeroIndex > maxi:
                    maxi = i - prevZeroIndex
                    maxIndex = i
            else:
                if i - prevPrevZeroIndex > maxi:
                    maxi = i - prevPrevZeroIndex
                    maxIndex = prevZeroIndex
        if a[i] == 0:
            prevZeroIndex, prevPrevZeroIndex = i, prevZeroIndex
    return maxIndex


a = [1, 1, 0, 1, 0, 1, 1, 1, 1, 0]
print(findIndex(a))

