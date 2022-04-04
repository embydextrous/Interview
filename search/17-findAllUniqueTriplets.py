def findUniqueTriplets(a, x):
    # Two implement two pointer algorithm
    a.sort()
    n = len(a)
    triplets = []
    for i in range(n - 2):
        # fixes ith element so we need to find if x - a[i] sum exists in remaining array
        l = i + 1
        r = n - 1
        # All triplets starting with same i already processed
        if i != 0 and a[i] == a[i-1]:
            continue
        while l < r:
            if a[l] + a[r] + a[i] == x:
                triplets.append([a[i], a[l], a[r]])
                # We don't need same value of a[l] now.
                while l < r:
                    if a[l] != a[l + 1]:
                        l += 1
                        break
                    l += 1
                while l < r:
                    if a[2] != a[r - 1]:
                        r -= 1
                        break
                    r -= 1
            elif a[l] + a[r] + a[i] < x:
                l += 1
            else:
                r -= 1
    return triplets

a = [1, 7, 7, 7, 8, 8, 8, 8]
x = 26
print(findUniqueTriplets(a, 16))