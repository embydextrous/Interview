def elementAtIndexAfterGivenRotations(a, ranges, index):
    for (l, r) in ranges[::-1]:
        if index == l:
            index = r
        elif index <= r and index > l:
            index = index - 1
    return a[index]


a = [1, 2, 3, 4, 5]
print(elementAtIndexAfterGivenRotations(a, [[0, 2], [0, 3]], 4))