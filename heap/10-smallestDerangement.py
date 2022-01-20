import heapq

# for n = 3 sequence is 123, for n = 4 sequence is 1234
def smallestDerangement(n):
    result = [i for i in range(1, n+1)]
    j = 0
    while j < n - 1:
        result[j+1], result[j] = result[j], result[j+1]
        j += 2
    if j == n - 1:
        result[j], result[j-1] = result[j-1], result[j]
    return result

print(smallestDerangement(5))

