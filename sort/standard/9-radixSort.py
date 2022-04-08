def countSort(a, exp):
    n = len(a)
    output = [0] * n
    count = [0] * 10
    for i in a:
        idx = (i // exp) % 10
        count[idx] += 1
    # For each position store index of first next index
    for i in range(1, 10):
        count[i] += count[i-1]
    # Start from reverse to keep order of elements intact
    i = n - 1
    while i >= 0:
        idx = (a[i] // exp) % 10
        output[count[idx] - 1] = a[i]
        count[idx] -= 1
        i -= 1
    for i in range(n):
        a[i] = output[i]
    print(a)

def radixSort(a):
    maxi = max(a)
    exp = 1
    while maxi / exp > 1:
        countSort(a, exp)
        exp *= 10

a = [170, 45, 75, 90, 802, 24, 2, 66]
radixSort(a)
#print(a)