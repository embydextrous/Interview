import heapq
from random import randint

class Median:
    def __init__(self):
        self.minHeap = []
        self.maxHeap = []
        self.median = None

    def process(self, x):
        if self.median is None:
            self.median = x
            self.maxHeap.append(x * -1)
            return
        if len(self.minHeap) < len(self.maxHeap):
            if x > self.maxHeap[0] * -1:
                heapq.heappush(self.minHeap, x)
            else:
                heapq.heappush(self.minHeap, -1 * heapq.heappop(self.maxHeap))
                heapq.heappush(self.maxHeap, -1 * x)
            self.median = (-1 * self.maxHeap[0] + self.minHeap[0]) / 2
            return
        if len(self.maxHeap) < len(self.minHeap):
            if x < self.minHeap[0]:
                heapq.heappush(self.maxHeap, x * -1)
            else:
                heapq.heappush(self.maxHeap, -1 * heapq.heappop(self.minHeap))
                heapq.heappush(self.minHeap, x)
            self.median = (-1 * self.maxHeap[0] + self.minHeap[0]) / 2
            return
        if x > self.median:
            heapq.heappush(self.minHeap, x)
            self.median = self.minHeap[0]
        else:
            heapq.heappush(self.maxHeap, -1 * x)
            self.median = -1 * self.maxHeap[0]



a = []
m = Median()
for i in range(11):
    x = randint(1, 20)
    a.append(x)
    m.process(x)
    print(a, m.median)
