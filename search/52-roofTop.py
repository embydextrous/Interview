# https://www.geeksforgeeks.org/roof-top/

def countSteps(a):
    maxSteps = 0
    n = len(a)
    i = 1
    while i < n:
        c = 0
        while i < n and a[i] > a[i-1]:
            c += 1
            i += 1
        maxSteps = max(maxSteps, c)
        i += 1
    return maxSteps

a = [4, 4, 4, 4]
print(countSteps(a))