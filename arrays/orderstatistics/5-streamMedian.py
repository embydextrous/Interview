from heapq import heappush, heappop
from random import randint

class Median:
    def __init__(self):
        self.minHeap = []
        self.maxHeap = []
        self.median = None

    def process(self, x):
        if self.median is None:
            heappush(self.maxHeap, -1 * x)
            self.median = x
        elif len(self.maxHeap) > len(self.minHeap):
            if x >= self.median:
                heappush(self.minHeap, x)
            else:
                heappush(self.minHeap, -1 * heappop(self.maxHeap))
                heappush(self.maxHeap, -1 * x)
            self.median = (self.minHeap[0] + -1 * self.maxHeap[0]) / 2
        elif len(self.minHeap) > len(self.maxHeap):
            if x <= self.median:
                heappush(self.maxHeap, -1 * x)
            else:
                heappush(self.maxHeap, -1 * heappop(self.minHeap))
                heappush(self.minHeap, x)
            self.median = (self.minHeap[0] + -1 * self.maxHeap[0]) / 2
        else:
            if x <= self.median:
                heappush(self.maxHeap, -1 * x)
                self.median = -1 * self.maxHeap[0]
            else:
                heappush(self.minHeap, x)
                self.median = self.minHeap[0]


median = Median()
a = [randint(1, 50) for i in range(20)]
print(a)
for i in a:
    median.process(i)
    print(median.median)