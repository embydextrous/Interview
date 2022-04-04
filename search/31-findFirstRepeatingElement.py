'''
Given an array of integers, find the first repeating element in it. 
We need to find the element that occurs more than once and whose index of first occurrence is smallest.

Input:  arr[] = {10, 5, 3, 4, 3, 5, 6}
Output: 5 [5 is the first element that repeats]

Input:  arr[] = {6, 10, 5, 4, 9, 120, 4, 6, 10}
Output: 6 [6 is the first element that repeats]
'''
# Hash Solution
# Can be also solved my making copy of array sorting it and for each element finding if it repeats.
def firstRepeating(a):
    d = {}
    firstRepeatingIndex = -1
    for i in range(len(a)):
        if a[i] in d:
            if firstRepeatingIndex == -1:
                firstRepeatingIndex = d[a[i]]
            else:
                firstRepeatingIndex = min(firstRepeatingIndex, d[a[i]])
        else:
            d[a[i]] = i
    if i == -1:
        return None
    return a[firstRepeatingIndex]

# Sort Based Solution
def firstRepeating2(a):
    copyA = a[:]
    copyA.sort()
    for i in a:
        if repeats(copyA, 0, len(a) - 1, i):
            return i
    return None

def repeats(a, l, r, x):
    if l > r:
        return False
    m = l + (r - l) // 2
    if a[m] == x and m > l and a[m] == a[m-1]:
        return True
    if a[m] == x and m < r and a[m] == a[m+1]:
        return True
    if a[m] > x:
        return repeats(a, l, m - 1, x)
    return repeats(a, m + 1, r, x)
    
a = [6, 10, 5, 4, 9, 120, 4, 6, 10]
print(firstRepeating2(a))
