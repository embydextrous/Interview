import heapq

def mergeTwoMaxHeaps(a, b):
    result = []
    for i in a:
        result.append(i * -1)
    for i in b:
        result.append(i * -1)
    heapq.heapify(result)
    return [-1 * i for i in result]

a = [10, 5, 6, 2]
b = [12, 7, 9]
print(mergeTwoMaxHeaps(a, b))
