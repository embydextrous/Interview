# https://www.geeksforgeeks.org/sum-matrix-element-absolute-difference-row-column-numbers/

def findSum(n):
    sum = 0
    multiplier = 2
    for i in range(n-1, 0, -1):
        sum += i * multiplier
        multiplier += 2
    return sum

print(findSum(7))