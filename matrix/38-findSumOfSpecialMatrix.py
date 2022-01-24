# https://www.geeksforgeeks.org/sum-matrix-element-element-integer-division-row-column/

def findSum(n):
    sum = 0
    for i in range(n):
        if i == 0:
            sum += (n * (n + 1)) // 2
        else:
            s = n - i
            toAdd = 1
            while s > 0:
                multiplier = min(i + 1, s)
                sum += toAdd * multiplier
                toAdd += 1
                s -= multiplier
    return sum

print(findSum(5))
