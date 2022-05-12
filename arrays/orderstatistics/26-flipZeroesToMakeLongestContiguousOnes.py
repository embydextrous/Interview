'''
Given a binary array and an integer m, find the position of zeroes flipping which 
creates maximum number of consecutive 1's in array.
Examples : 
 

Input:   arr[] = {1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1}
         m = 2
Output:  5 7
We are allowed to flip maximum 2 zeroes. If we flip
arr[5] and arr[7], we get 8 consecutive 1's which is
maximum possible under given constraints 

Input:   arr[] = {1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1}
         m = 1
Output:  7
We are allowed to flip maximum 1 zero. If we flip 
arr[7], we get 5 consecutive 1's which is maximum 
possible under given constraints.

Input:   arr[] = {0, 0, 0, 1}
         m = 4
Output:  0 1 2
Since m is more than number of zeroes, we can flip
all zeroes.
'''

def zeroesToBeFlipped(a, m):
    n = len(a)
    l = r = 0
    bestL = bestWindow = 0
    zeroCount = 0
    while r < n:
        if zeroCount <= m:
            if a[r] == 0:
                zeroCount += 1
            r += 1

        if zeroCount > m:
            if a[l] == 0:
                zeroCount -= 1
            l += 1

        if zeroCount <= m and r - l > bestWindow:
            bestL = l
            bestWindow = r - l
    zeroes = []
    for i in range(bestL, bestL + bestWindow):
        if a[i] == 0:
            zeroes.append(i)
    return zeroes

a = [1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1]
print(zeroesToBeFlipped(a, 2))
