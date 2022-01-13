import heapq

def findMax(a, k):
    minHeap = a[:k]
    heapq.heapify(minHeap)
    num = len(a) - k + 1
    for i in range(num):
        print(minHeap[0], end = " ")
        if i == num - 1:
            break
        enter, exit = a[i + k], a[i]
        for j in range(k):
            minDone = False
            if not minDone and minHeap[j] == exit:
                minHeap[j] = enter
                minDone = True
                heapq.heapify(minHeap)
            if minDone:
                break
    print()
    
a = [8, 5, 10, 7, 9, 4, 15, 12, 90, 13]
findMax(a, 4)
