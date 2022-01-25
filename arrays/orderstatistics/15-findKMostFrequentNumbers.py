import heapq

class HeapNode:
    def __init__(self, key, frequency):
        self.key = key
        self.frequency = frequency

    def __str__(self) -> str:
        return "HeapNode[key={}, frequency={}]".format(self.key, self.frequency)

    def __lt__(self, other):
        if self.frequency != other.frequency:
            return -1 * self.frequency < -1 * other.frequency
        else:
            return -1 * self.key < -1 * other.key

def kMostFrequentElements(a, k):
    d = {x : a.count(x) for x in a}
    print(d)
    h = []
    for key in d.keys():
        heapq.heappush(h, HeapNode(key, d[key]))
    for j in range(k):
        print(heapq.heappop(h).key, end = " ")
    print()

a = [7, 10, 11, 5, 2, 5, 5, 7, 11, 8, 9]
k = 4
kMostFrequentElements(a, k)