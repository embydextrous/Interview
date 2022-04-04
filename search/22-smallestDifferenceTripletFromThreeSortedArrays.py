import sys

# Also see, https://www.geeksforgeeks.org/smallest-difference-pair-values-two-unsorted-arrays/
# Sort the two arrays and follow same logic as here.
# Also see, https://www.geeksforgeeks.org/find-three-closest-elements-from-given-three-sorted-arrays/ (Same Solution)
def smallestDiffTriplet(a, b, c):
    i = j = k = 0
    mindiff = sys.maxsize
    triplet = None
    while i < len(a) and j < len(b) and k < len(c):
        mini = min(a[i], b[j], c[k])
        maxi = max(a[i], b[j], c[k])
        if maxi - mini < mindiff:
            mindiff = maxi - mini
            triplet = [a[i], b[j], c[k]]
        if a[i] == mini:
            i += 1
        elif b[j] == mini:
            j += 1
        else:
            k += 1
    return triplet

a = [20, 24, 100]
b = [2, 19, 22, 79, 800]
c = [10, 12, 23, 24, 119]
print(smallestDiffTriplet(a, b, c))