import heapq

# Also see, https://www.geeksforgeeks.org/minimum-product-k-integers-array-positive-integers/ (form heap and pop k)

def findSum(a, k1, k2):
    heapq.heapify(a)
    while k1 > 0:
        k1 -= 1
        k2 -= 1
        heapq.heappop(a)
    sum = 0
    while k2 > 1:
        k2 -= 1
        sum += heapq.heappop(a)
    return sum
    
k1 = 2
k2 = 6
a = [10, 2, 50, 12, 48, 13]
print(findSum(a, k1, k2))
