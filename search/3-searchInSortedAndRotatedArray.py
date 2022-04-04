def search(arr, l, r, x):
    if l > r:
        return -1
    m = l + (r - l) // 2
    if arr[m] == x:
        return m
    # Check if left subarray is sorted
    if arr[l] <= arr[m]:
        # x lies in left subarray
        if x >= arr[l] and x < arr[m]:
            return search(arr, l, m - 1, x)
        return search(arr, m + 1, r, x)
    # if left array is nor sorted, right must be sorted
    if x > arr[m] and x <= arr[r]:
        # x lies in right subarray
        return search(arr, m + 1, r, x)
    return search(arr, l, m - 1, x)

a = [5,1,3]
print(search(a, 0, len(a) - 1, 5))