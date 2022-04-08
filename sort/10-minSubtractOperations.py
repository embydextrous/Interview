'''
You are given a sequence of numbers arr[0], arr[1], …, arr[N - 1] and a positive integer K. 
In each operation, you may subtract K from any element of the array. You are required to find 
the minimum number of operations to make the given array decreasing.
An array arr[0], arr[1], ....., arr[N-1] is called decreasing if arr[i] >= arr[i+1] for each i: 0 <= i < N-1. 
    
    Input : N = 4, K = 5, arr[] = {1, 1, 2, 3} 
    Output : 3
'''
def count(a, k):
    count = 0
    n = len(a)
    for i in range(1, n):
        if a[i] > a[i-1]:
            if (a[i] - a[i-1]) % k == 0:
                c = (a[i] - a[i-1]) // k
            else:
                c = (a[i] - a[i-1]) // k + 1
            count += c
            a[i] -= c * k
    print(a)
    return count

a = [1, 8, 10, 6, 9, 12]
print(count(a, 3))