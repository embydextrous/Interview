from search import binarySearchUtil

def findTriplets(a):
    n = len(a)
    for i in range(n-1, 1, -1):
        l = 0
        r = i - 1
        while l < r:
            if a[l] + a[r] == a[i]:
                print(a[l], a[r], a[i])
                l += 1
                r -= 1
            elif a[l] + a[r] < a[i]:
                l += 1
            else:
                r -= 1
           
a = [1, 2, 4, 7, 9, 10, 12, 15, 18]
findTriplets(a)