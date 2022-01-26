import sys

def findMinDistance(a, x, y):
    lastIndex = -1
    xorValue = x ^ y
    valueToLookFor = xorValue
    minDistance = sys.maxsize
    for i in range(len(a)):
        if lastIndex == -1:
            if a[i] == x or a[i] == y:
                valueToLookFor ^= a[i]
                lastIndex = i
        else:
            if a[i] == valueToLookFor:
                minDistance = min(minDistance, i - lastIndex)
                valueToLookFor = xorValue ^ valueToLookFor
                lastIndex = i
            elif a[i] == xorValue ^ a[i]:
                lastIndex = i
    return minDistance

a = [3, 5, 4, 2, 6, 5, 6, 6, 5, 4, 8, 3]
x = 3
y = 1
print(findMinDistance(a, x, y))



