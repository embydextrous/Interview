'''
1. Counting sort is efficient if the range of input data is not significantly greater than the 
    number of objects to be sorted. Consider the situation where the input sequence is between range 
    1 to 10K and the data is 10, 5, 10K, 5K. 
2. It is not a comparison based sorting. It running time complexity is O(n) with space proportional to 
    the range of data. 
3. It is often used as a sub-routine to another sorting algorithm like radix sort. 
4. Counting sort uses a partial hashing to count the occurrence of the data object in O(1).
'''
# Time Complexity - O(n + k)
# Space Complexity - O(k) where k is range of data.
def countSort(a):
    maxi = max(a)
    mini = min(a)
    c = [0] * (maxi - mini + 1)
    for i in a:
        c[i-mini] += 1
    k = 0
    for i in range(len(c)):
        value = mini + i
        for j in range(c[i]):
            a[k] = value
            k += 1

a = [3, 1, -2, 5, 6, 4, 3, 2, 3, 4, 2, -1, 1, 2, -2, 4, 2]
countSort(a)
print(a)