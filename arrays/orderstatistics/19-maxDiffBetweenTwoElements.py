# https://www.geeksforgeeks.org/maximum-difference-between-two-elements/
# The problem is similar to atock buying and selling once
def findMaxDiff(a):
    mini = a[0]
    maxDiff = 0
    for i in range(1, len(a)):
        if a[i] < mini:
            mini = a[i]
        elif a[i] - mini > maxDiff:
            maxDiff = a[i] - mini
    return maxDiff

a = [4, 8, 1, 9, 7, 2, 11]
print(findMaxDiff(a))
