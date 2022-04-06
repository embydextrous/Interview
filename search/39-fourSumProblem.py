'''
Given an array of integers, find anyone combination of four elements in the 
array whose sum is equal to a given value X.

For example, 

Input: array = {10, 2, 3, 4, 5, 9, 7, 8} 
       X = 23 
Output: 3 5 7 8
'''

# Solution 1 - Fix first and second elements - linear search for next 2 - O(n^3)
def fourSum(a, x):
    a.sort()
    n = len(a)
    for i in range(n):
        for j in range(i + 1, n - 2):
            l = j + 1
            r = n - 1
            while l < r:
                if a[i] + a[j] + a[l] + a[r] == x:
                    return (a[i], a[j], a[l], a[r])
                elif a[i] + a[j] + a[l] + a[r] < x:
                    l += 1
                else:
                    r -= 1

# Solution 2 - 
def fourSum2(a, x):
    n = len(a)
    pairSumArray = []
    for i in range(n):
        for j in range(i + 1, n):
            pairSumArray.append(PairSumNode(a[i] + a[j], i, j))
    pairSumArray.sort()
    l = 0
    r = len(pairSumArray) - 1
    while l < r:
        s = pairSumArray[l].x + pairSumArray[r].x
        if s == x and pairSumArray[l].i != pairSumArray[r].i and pairSumArray[l].j != pairSumArray[r].j:
            (idx1, idx2, idx3, idx4) = pairSumArray[l].i, pairSumArray[l].j, pairSumArray[r].i, pairSumArray[r].j
            idxSet = set()
            idxSet.add(idx1)
            idxSet.add(idx2)
            idxSet.add(idx3)
            idxSet.add(idx4)
            if len(idxSet) == 4:
                return (a[idx1], a[idx2], a[idx3], a[idx4])
        if s == x:
            p = l + 1
            while p < r and pairSumArray[p].x == pairSumArray[l].x:
                q = r
                while q > l and pairSumArray[q].x == pairSumArray[r].x:
                    (idx1, idx2, idx3, idx4) = pairSumArray[p].i, pairSumArray[p].j, pairSumArray[q].i, pairSumArray[q].j
                    idxSet = set()
                    idxSet.add(idx1)
                    idxSet.add(idx2)
                    idxSet.add(idx3)
                    idxSet.add(idx4)
                    if len(idxSet) == 4:
                        return (a[idx1], a[idx2], a[idx3], a[idx4])
                    q -= 1
                p += 1
            l = p
            r = q
            if pairSumArray[l].x == pairSumArray[l+1].x:
                l += 1
            elif pairSumArray[r].x == pairSumArray[r-1].x:
                r -= 1
            else:
                return None
        elif s < x:
            l += 1
        else:
            r -= 1

class PairSumNode:
    def __init__(self, x, i, j):
        self.x = x
        self.i = i
        self.j = j

    def __le__(self, other):
        return self.x <= other.x

    def __lt__(self, other):
        return self.x < other.x

    def __repr__(self):
        return "x=" + str(self.x) + ";i=" + str(self.i) + ";j=" + str(self.j)

a = [10, 2, 3, 4, 5, 9, 7, 8]
x = 25
print(fourSum(a, x))

# [2, 3, 4, 5, 7, 8, 9, 10]